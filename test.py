class Limit:
    def __init__(self, val):
        self.val = val
        self.left_child = None
        self.right_child = None


def insert_limit(current_node: Limit | None, new_node: Limit):
    if current_node is None:
        return new_node
    if current_node.val < new_node.val:
        current_node.right_child = insert_limit(current_node.right_child, new_node)
    else:
        current_node.left_child = insert_limit(current_node.left_child, new_node)
    return current_node

root = None
x = [Limit(5), Limit(2), Limit(7), Limit(4), Limit(1), Limit(6), Limit(8)]
for i in x:
    root = insert_limit(root, i)

current = root
while current is not None:
    print(f"current: {current.val}, {current.left_child.val}, {current.right_child.val}")
    current = current.right_child