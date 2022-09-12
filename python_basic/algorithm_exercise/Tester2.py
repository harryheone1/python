class TreeNode:
    def __init__(self, val: int, children: list[int] = []):
        self.val = val
        self.children = children

def min_mask_distributor(root: TreeNode) -> int:
    distribute_count = 0

    def dfs(node) -> int:
        nonlocal distribute_count
        # base case
        if not node.children:
            return 0

        min_state = float('inf')
        max_state = float('-inf')
        for child in node.children:
            state = dfs(child)

        min_state = min(min_state, state)
        max_state = max(max_state, state)
        if min_state == 0:
            distribute_count += 1
            return 2
        if max_state == 2:
            return 1

        return 0

    if dfs(root) == 0:
        distribute_count += 1
    return distribute_count


if __name__ == "__main__":

    #               CEO  2
    #      VP1              VP2  0
    # Manager1 Manager2
    # manager1 = TreeNode(0)
    # manager2 = TreeNode(1)
    # vp2 = TreeNode(2)
    #
    # vp1 = TreeNode(3, [manager1, manager2])
    #
    # ceo = TreeNode(4, [vp1, vp2])


    # Test case 2
    engineer1 = TreeNode(0)
    engineer2 = TreeNode(1)
    manager1 = TreeNode(2, [engineer1, engineer2])

    manager2 = TreeNode(3)
    manager3 = TreeNode(4)
    manager4 = TreeNode(5)
    manager5 = TreeNode(6)

    vp1 = TreeNode(2, [manager1, manager2])
    vp2 = TreeNode(3, [manager3, manager4, manager5])

    svp1 = TreeNode(2, [vp1])
    svp2 = TreeNode(3, [vp2])

    ssvp1 = TreeNode(2, [svp1, svp2])
    ssvp2 = TreeNode(1)

    ceo = TreeNode(4, [ssvp1, ssvp2])
    board = TreeNode(4, [ceo])
    board2 = TreeNode(4, [board])

    print(min_mask_distributor(board2))