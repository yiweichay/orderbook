import pytest 
from book import Book
from order import Order

def test_add_limit_order_to_tree():
    book = Book()
    a = Order(1, True, 50, 100, 1)
    b = Order(2, True, 20, 102, 2)
    c = Order(3, True, 30, 100, 3)
    d = Order(4, True, 15, 98, 4)
    e = Order(5, True, 15, 97, 5)
    f = Order(6, True, 5, 101, 6)

    book.add_limit_order_to_tree(a)
    assert book.buy_tree.limit_price == a.limit
    assert book.highest_buy.limit_price == a.limit
    assert book.buy_tree.head_order == book.buy_tree.tail_order

    book.add_limit_order_to_tree(b)
    assert book.buy_tree.right_child.limit_price == b.limit
    assert book.highest_buy.limit_price == b.limit

    book.add_limit_order_to_tree(c)
    assert book.buy_tree.tail_order == c
    assert book.buy_tree.left_child == None

    book.add_limit_order_to_tree(d)
    assert book.buy_tree.left_child.limit_price == d.limit

    book.add_limit_order_to_tree(e)
    assert book.buy_tree.left_child.left_child.limit_price == e.limit
    
    book.add_limit_order_to_tree(f)
    assert book.buy_tree.right_child.left_child.limit_price == f.limit
