from limit import Limit
from order import Order

# A book has all the different limits stored as a binary search tree
class Book:
    def __init__(self) -> None:
        self.buy_tree: Limit = None
        self.sell_tree: Limit = None
        self.highestBuy: Limit = None
        self.lowestSell: Limit = None

        self.limit_map: dict = {}
        self.order_map: dict = {}

    def add_limit_order_to_tree(self, order: Order):
        if order.is_buy:
            self.buy_tree = insert_limit(self.buy_tree, Limit(order))
        else:
            self.sell_tree = insert_limit(self.sell_tree, Limit(order))
                
def insert_limit(current_node: Limit | None, new_node: Limit):
    if current_node is None:
        return new_node
    if current_node.limit_price < new_node.limit_price:
        insert_limit(current_node.right_child, new_node)
    else:
        insert_limit(current_node.left_child, new_node)
    return current_node

'''
a: buy, $2, 5
b: buy $2, 3
c: buy $3, 10
d: sell $2, 3
e: buy $1, 1
'''