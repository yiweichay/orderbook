from limit import Limit

class Order:
    def __init__(
            self,
            id_number: int,
            is_buy: bool,
            shares: int,
            limit: int, #price of the order
            timestamp: int
    ) -> None:
        self.id_number: int = id_number
        self.is_buy: bool = is_buy
        self.share: int = shares
        self.limit: int = limit
        self.timestamp: int = timestamp
        self.next_order: 'Order' = None
        self.prev_order: 'Order' = None
        self.parent_limit: Limit = None
