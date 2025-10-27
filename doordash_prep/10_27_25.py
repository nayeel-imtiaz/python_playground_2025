"""
START: 1:47 pm - 2:24 pm

Design a food-delivery order service

CONTINUE: 2:34 pm - 3:05 pm (I was a bit dosed off, and main time blocker
was figuring out how to map orders and customer_ids together)

important variables/classes to make:
- dictionary (active_orders) where order_id -> `Order` object
- create a class called `Order` that contains the following info:
    - order_id (int)
    - customer_id (int)
    - items (list[str])
    - driver_id (-1 or None if no driver assigned)
    - status (ex: "delivered", "order placed", "driver picked up food")

methods to make:

create_order(customer_id: int, items: list[str]) -> None
- Have a dictionary (customer_orders) where order_id -> `Order` object
- This method will create/update the customer_orders dictionary

assign_driver(order_id: int, driver_id: int)
- Update driver_id attribute in correct Order object from
  `customer_orders` dictionary

update_status(order_id: int, new_status)
- Update status by updating status attribute in correct
  order_id object in `customer_orders` dictionary

get_orders_by_customer(customer_id) -> list[str]
- this method will return a customer's order

"""

from collections import defaultdict

class Order:
    def __init__(self, order_id, customer_id, items, driver_id=-1, status=""):
        self.order_id = order_id
        self.customer_id = customer_id
        self.items = items
        self.driver_id = driver_id
        self.status = status

    def __repr__(self):
        return repr(self)


class Doordash:
    def __init__(self):
        self.order_counter = 1
        self.active_orders = {}
        self.customer_orders = defaultdict(list)  # map customer id to their list of order ids

    def create_order(self, customer_id: int, items: list[str]) -> None:
        new_order = Order(self.order_counter, customer_id, items)
        self.active_orders[new_order.order_id] = new_order
        self.customer_orders[new_order.customer_id].append(new_order.order_id)
        self.order_counter += 1

    def assign_driver(self, order_id: int, driver_id: int) -> None:
        self.active_orders[order_id].driver_id = driver_id

    def update_status(self, order_id: int, new_status: str) -> None:
        self.active_orders[order_id] = new_status

    def get_orders_by_customer(self, customer_id: int) -> list[str]:
        return [self.active_orders[order_id] for order_id in self.customer_orders[customer_id]]




