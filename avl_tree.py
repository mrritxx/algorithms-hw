class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


def height(node):
    if node is None:
        return 0
    return node.height


def update(node):
    node.height = 1 + max(height(node.left), height(node.right))


def rotate_right(node):
    new_root = node.left
    node.left = new_root.right
    new_root.right = node
    update(node)
    update(new_root)
    return new_root


def rotate_left(node):
    new_root = node.right
    node.right = new_root.left
    new_root.left = node
    update(node)
    update(new_root)
    return new_root


def insert(node, value):
    if node is None:
        return Node(value)
    if value < node.value:
        node.left = insert(node.left, value)
    else:
        node.right = insert(node.right, value)

    update(node)
    balance = height(node.left) - height(node.right)

    if balance > 1:
        if value > node.left.value:
            node.left = rotate_left(node.left)
        return rotate_right(node)
    if balance < -1:
        if value < node.right.value:
            node.right = rotate_right(node.right)
        return rotate_left(node)
    return node


def to_list(node):
    if node is None:
        return []
    return to_list(node.left) + [node.value] + to_list(node.right)
