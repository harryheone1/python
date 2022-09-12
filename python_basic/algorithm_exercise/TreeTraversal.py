def pre_order(node):
    print(node)
    if node.left() is not None:
        pre_order(node.left())
    if node.right() is not None:
        pre_order(node.right())


def pre_order_loop(root):
    node_stack = []
    node = access_and_left(root, node_stack)
    # first print then go to left continuously
    while len(node_stack) != 0:
        if node is not None:
            node = access_and_left(root, node_stack)
        else:
            node = pop_and_right(node_stack)
            # pop out current node and go to right atomically


def access_and_left(node, tree_stack):
    print(node)
    tree_stack.append(node)
    if node.left is not None:
        return node.left


def pop_and_right(tree_stack):
    poped = tree_stack.pop()
    if poped == tree_stack[len(tree_stack) - 1].left():
        return tree_stack[len(tree_stack) - 1].right()
    if poped == tree_stack[len(tree_stack) - 1].right():
        return None
    raise ValueError("There is problem in the algorithm")


def in_order(node):
    if node.left() is not None:
        in_order(node.left())
    print(node)
    if node.right() is not None:
        in_order(node.right())


def post_order(node):
    if node.left() is not None:
        in_order(node.left())
    print(node)
    if node.right() is not None:
        in_order(node.right())
