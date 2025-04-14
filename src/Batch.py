from src.Order import Order


class Batch:
    def __init__(self, artickle, color, size, quatity: int):
        self.artickle = artickle
        self.color = color
        self.size = size
        self.quatity = quatity
        self._orders = set()

    def place_order(self, order: Order):
        if (self.can_place_order(order)):
            self._orders.add(order)

    def remove_order(self, order: Order):
        if (order in self._orders):
            self._orders.remove(order)

    def can_place_order(self, order: Order) -> bool:
        return self.sku == order.sku and self.available - order.quatity >= 0

    def list_orders(self) -> list:
        return list(self._orders)

    @property
    def sum_ordered(self) -> int:
        return sum(order.quatity for order in self._orders)

    @property
    def available(self) -> int:
        return self.quatity - self.sum_ordered

    @property
    def sku(self):
        return f'{self.artickle}-{self.color}-{self.size}'

    def __str__(self):
        return f'{self.sku}, {self.available}'
