'''
Design and implement an in-memory food-delivery order service.

Your task is to model orders placed by customers and provide operations to create, update, and retrieve them.
You should design classes and methods that could realistically represent a simple backend service.

Important variables/classes/data structures:
- `Order` class to track the following:
    - order_id (int)
    - customer_id (int)
    - driver_id (int)
    - status (str)
    - items (list[str])

- Dictionary to map `customer_id` -> list[Order]
    - {
        100: [Order(), Order()]
    }

- Dictionary to map order_id -> Order
  - {
        955: Order(order_id: 955)
  }

Operations to support:
- creating new order
    - create_order(customer_id: int, items: list[str]) -> int (order_id)

- assign driver
    - assign_driver(driver_id: int, order_id: int) -> bool

- update the order status
    - update_status(new_status: str, order_id) -> bool

- get all orders for given customer


'''


from collections import defaultdict

class Order:
    def __init__(self, order_id: int, customer_id: int, items: list[str], driver_id: int = -1, status: str = "CREATED"):
        self.order_id = order_id
        self.customer = customer_id
        self.items = items
        self.driver_id = driver_id
        self.status = status


class DoorDash:
    def __init__(self):
        self.active_orders = {}
        self.customers_orders = defaultdict(list)
        self.order_counter = 1

    def create_order(self, customer_id: int, items: list[str]) -> int:
        new_order = Order(self.order_counter, customer_id, items)
        self.active_orders[self.order_counter] = new_order
        self.customers_orders[customer_id].append(new_order)
        self.order_counter += 1
        return new_order.order_id

    def assign_driver(self, driver_id: int, order_id: int) -> bool:
        order = self.active_orders.get(order_id)
        if order:
            order.driver_id = driver_id
            return True
        else:
            return False

    def update_status(self, new_status: str, order_id) -> bool:
        pass

    def get_orders_for_customer(self, customer_id: int) -> list[Order]:
        pass
