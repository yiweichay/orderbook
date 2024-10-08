'''
Order is a single order submitted by the buyer/seller
'''

class Order:
    def __init__(
            self,
            id_number: int,
            is_buy: bool,
            shares: int, #units
            limit: int, #price of the order
            timestamp: int
    ) -> None:
        self.id_number: int = id_number
        self.is_buy: bool = is_buy
        self.shares: int = shares
        self.limit: int = limit #the price of the order
        self.timestamp: int = timestamp
        self.next_order: 'Order' = None
        self.prev_order: 'Order' = None