from limit import Limit
from order import Order

# A book has all the different limits stored as a binary search tree
class Book:
    def __init__(self) -> None:
        self.buy_tree: Limit = None
        self.sell_tree: Limit = None
        self.highest_buy: Limit = None
        self.lowest_sell: Limit = None

        self.limit_map: dict = {}
        self.order_map: dict = {}

    def add_limit_order_to_tree(self, order: Order):
        limit = self.limit_map.get(order.limit)
        # if limit is not present and node not in tree
        if not limit:
            limit = Limit(order)
            self.limit_map[order.limit] = limit #Add limit order to the limit map for O(n) search time in dict
            if order.is_buy:
                self.buy_tree = insert_limit(self.buy_tree, limit)
                if not self.highest_buy or order.limit > self.highest_buy.limit_price:
                    self.highest_buy = limit
            else:
                self.sell_tree = insert_limit(self.sell_tree, Limit(order))
                if not self.lowest_sell or order.limit < self.lowest_sell.limit_price:
                    self.lowest_sell = limit
        # if limit is present and node in tree 
        else:
            order.prev_order = limit.tail_order
            limit.tail_order.next_order = order
            limit.tail_order = order
    
    def delete_limit_order_from_tree(self, order: Order):
        pass
                
def insert_limit(current_node: Limit | None, new_node: Limit):
    if current_node is None:
        return new_node
    if current_node.limit_price < new_node.limit_price:
        current_node.right_child = insert_limit(current_node.right_child, new_node)
    else:
        current_node.left_child = insert_limit(current_node.left_child, new_node)
    return current_node

def delete_limit_sell_tree(current_node: Limit | None):
    if current_node.parent:
        if current_node.right_child == None:
            current_node.parent.left_child = None
            return current_node.parent
        else:
            current_node.parent.left_child = current_node.right_child
            return current_node.right_child
    else:
        current_node.right_child.parent = None
        temp = current_node.right_child
        while temp.left_child:
            temp = temp.left_child
        return temp
            
def delete_limit_buy_tree(current_node: Limit | None):
    if current_node.parent:
        if current_node.left_child == None:
            current_node.parent.right_child = None
            return current_node.parent
        else:
            current_node.parent.right_child = current_node.left_child
            return current_node.left_child
    else:
        current_node.left_child.parent = None
        temp = current_node.left_child
        while temp.right_child:
            temp = temp.right_child
        return temp

'''
a: buy, $2, 5
b: buy $2, 3
c: buy $3, 10
d: sell $2, 3
e: buy $1, 1
'''