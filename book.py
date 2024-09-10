from limit import Limit
from order import Order

'''
A book has all the different limits stored as a binary search tree
Book -> Limit -> Order
'''

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
        self.order_map[order.id_number] = order
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
            limit.total_volume += order.shares
    
    def delete_limit_order_from_tree(self, order: Order):
        # buy order, remove from sell tree
        # sell order, remove from buy tree
        shares_to_delete = order.shares
        if order.is_buy:
            # this is for limit orders, because it will delete until the limit
            # for market orders, we can set limit = 0, so there is no limit price
            while shares_to_delete and self.lowest_sell and order.limit >= self.lowest_sell.limit_price:
                # if the shares to delete is more than the total volume available in a limit, delete the whole limit
                if shares_to_delete >= self.lowest_sell.total_volume:
                    del self.limit_map[self.lowest_sell]
                    current_order = self.lowest_sell.head_order
                    # delete all the order ids from the order map (the whole linked list of each limit)
                    while current_order:
                        del self.order_map[current_order.id]
                        current_order = current_order.next_order
                    shares_to_delete -= self.lowest_sell.total_volume
                    self.lowest_sell = delete_limit_sell_tree(self.lowest_sell)

                # if shares to delete is lesser than volume available in the limit
                else:
                    current_order = self.lowest_sell.head_order
                    while shares_to_delete:
                        # check the head order to see if the units are more or less than shares to delete
                        if shares_to_delete < current_order.shares:
                            current_order.shares -= shares_to_delete
                            self.lowest_sell.total_volume -= shares_to_delete
                            shares_to_delete = 0
                        else:
                            del self.order_map[current_order.id]
                            current_order.next_order.prev_order = None
                            self.lowest_sell.total_volume -= current_order.shares
                            shares_to_delete -= current_order.shares
                            current_order = current_order.next_order
                            self.lowest_sell.head_order = current_order
                        

                
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