from order import Order

# Limit stores all orders at a given price
class Limit:
    def __init__(
            self,
            first_order: Order,
            parent: 'Limit' = None
    ) -> None:
        self.limit_price: int = first_order.limit
        self.size: int = 1
        self.total_volume: int = first_order.shares
        self.parent: 'Limit' = parent
        self.left_child: 'Limit' = None
        self.right_child: 'Limit' = None
        self.head_order: Order = first_order
        self.tail_order: Order = first_order
