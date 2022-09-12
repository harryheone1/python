class TreeNode:
    def __init__(self, val: int = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 1
# 2 3
# 4 5 6 7

def preorder(root: TreeNode):
    # 1) base case: all possible solutions
    if not root:
        return

    # 2) operations
    print(root.val)

    # 3) different options
    preorder(root.left)
    preorder(root.right)


def inorder(root: TreeNode):
    # 1) base case: all possible solutions
    if not root:
        return

    # 3) different options
    inorder(root.left)
    # 2) operations
    print(root.val)
    inorder(root.right)


def postorder(root: TreeNode):
    # 1) base case: all possible solutions
    if not root:
        return

    # 3) different options
    postorder(root.left)
    postorder(root.right)
    # 2) operations
    print(root.val)


if __name__ == '__main__':
    leaf1 = TreeNode(4)
    leaf2 = TreeNode(5)
    leaf3 = TreeNode(6)
    leaf4 = TreeNode(7)

    parent1 = TreeNode(2, leaf1, leaf2)
    parent2 = TreeNode(3, leaf3, leaf4)

    root = TreeNode(1, parent1, parent2)

    preorder(root)
    inorder(root)
    postorder(root)
