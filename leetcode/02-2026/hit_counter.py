'''
Problem: Event Rate Counter (Hit Counter, production-ish)

You’re building a lightweight metrics component used by multiple services to track event volume in near real-time.

Events arrive as (timestamp_seconds, eventType, tenantId) where:

timestamp_seconds is a Unix timestamp in seconds (monotonic most of the time, but may have small out-of-order jitter)

eventType is a string (e.g., "page_view", "api_call")

tenantId is a string (customer/org ID)

You need to support queries like:

“How many api_call events did tenant A have in the last 5 minutes?”

“How many total events did tenant B have in the last 60 seconds?”

“How many events of any type happened globally in the last 300 seconds?”

Requirements

Implement a class EventCounter with these operations:

record(timestamp: int, tenantId: str, eventType: str) -> None
count_last(timestamp: int, windowSec: int, tenantId: Optional[str], eventType: Optional[str]) -> int

Where:

count_last(t, w, tenantId, eventType) returns the number of events with timestamp in (t - w, t].

If tenantId is None, it means “all tenants”.

If eventType is None, it means “all event types”.

You can assume windowSec <= 3600 (at most 1 hour).

You should optimize for many reads and many writes.

Example

Suppose we record:

record(100, "A", "api_call")

record(101, "A", "api_call")

record(102, "A", "page_view")

record(160, "B", "api_call")

Queries:

count_last(102, 5, "A", "api_call") → 2 (timestamps 98..102: two api_calls at 100,101)

count_last(102, 60, "A", None) → 3 (A had 3 events in 42..102)

count_last(160, 300, None, "api_call") → 3 (api_call at 100,101,160)

count_last(160, 10, "A", None) → 0 (A has nothing in 150..160)

Constraints (what an interviewer will “casually” add)

Throughput: up to 200k events/sec across all tenants (you don’t need to implement concurrency, but design should be concurrency-friendly).

Cardinality: up to 100k tenants, event types could be dozens to hundreds.

Memory: you can only keep the last hour worth of data in memory (older can be discarded).

Out-of-order: events can arrive up to 2 seconds late (e.g., an event with timestamp 100 might arrive when current time is 102).

Latency: count_last should be fast (ideally O(1) or close).
'''

'''
Questions:
1) Can both tenant and event_type be passed in NULL? - yes?
2) Can we assume passed in time will be ints and not floats (second precision)? - Yes

# 9:58 pm
Model:
array of timestamp buckets (len of 3600): time_stamps
- at each index: {
    timestamp (int),
    global_counter (int),
    event_counts: dict[event type, int],
    tenant_count: dict[tenant_id, int],
    event_tenant_count: dict[(event type, tenant id), int],
}

Approach:
record(): access timestamp array via index [time % 3600] and update timestamp buckets
    - when bucket.timestamp != time: clear timestamp bucketelaborate on the equation if the event is too old for a record, like t is less than or equal to now, less than minus 3,600. What's the difference between t and now? I don't get it.
1. 2. Can you elaborate on the space complexity? Like why do we sum it up instead of multiplying? I didn't quite get that but it does make sense to include a distinct number of keys in that space complexity.
count_last(): we'll iterate through timestamp array and keep a running total

Edge cases:
- Count_last for last 0 seconds -> return 0
- Count_last for last 3600 seconds -> return sum of all the timestamp objects

Complexities:
Time:
    record(): O(1)
    count_last(): O(W) where W is window size,
    and since W ≤ 3600, this is O(1) in practice.
Space: O(3600 + distinct keys in last hour)
'''
from collections import defaultdict
import time
from typing import Optional

class TimeStamp:
    def __init__(self, timestamp: int):
        self.timestamp = timestamp
        self.global_counter = 0
        self.event_counts = defaultdict(int)
        self.tenant_counts = defaultdict(int)
        self.event_tenant_counts = defaultdict(int)


class EventCounter:
    def __init__(self):
        self.array_ring = [TimeStamp(0) for _ in range(3600)]

    def record(self, timestamp: int, eventType: str, tenantId: str) -> None:
        if self.array_ring[timestamp % 3600].timestamp != timestamp:
            self.array_ring[timestamp % 3600] = TimeStamp(timestamp)

        self.array_ring[timestamp % 3600].global_counter += 1
        self.array_ring[timestamp % 3600].event_counts[eventType] += 1
        self.array_ring[timestamp % 3600].tenant_counts[tenantId] += 1
        self.array_ring[timestamp % 3600].event_tenant_counts[(eventType, tenantId)] += 1


    def count_last(self, timestamp: int, windowSec: int, eventType: Optional[str], tenantId: Optional[str]) -> int:
        begin_time_index = (timestamp - windowSec + 1) % 3600
        end_time_index = timestamp % 3600
        event_count = 0
        for time_index in range(begin_time_index, end_time_index + 1):
            if eventType and tenantId:
                event_count += self.array_ring[time_index].event_tenant_counts[(eventType, tenantId)]
            elif eventType:
                event_count += self.array_ring[time_index].event_counts[eventType]
            elif tenantId:
                event_count += self.array_ring[time_index].tenant_counts[tenantId]
            else:
                event_count += self.array_ring[time_index].global_counter
        return event_count

start = time.time()
print(f"program start: {start}")

event_counter = EventCounter()
for _ in range(700):
    event_counter.record(timestamp=int(time.time()), eventType="page_view", tenantId="snowflake_customer")
for _ in range(500):
    event_counter.record(timestamp=int(time.time()), eventType="api_call", tenantId="snowflake_customer")

print(event_counter.count_last(timestamp=int(time.time()), windowSec=0, eventType="page_view", tenantId="snowflake_customer")) # 700
print(event_counter.count_last(timestamp=int(time.time()), windowSec=20, eventType="api_call", tenantId="snowflake_customer")) # 500

end = time.time()
print(f"program end: {end}")
print(f"took {end - start} seconds")