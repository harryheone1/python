class ListNode:
    def __init__(self, val: int, next=None):
        self.val = val
        self.next = next


def reverseKGroup(head: ListNode, k: int) -> ListNode:
    prev, cur, rs, successor = None, head, head, None

    def reverseK(node: ListNode, count: int) -> ListNode:
        nonlocal successor
        nonlocal prev

        if count + 1 == k:
            successor = node.next
            return node

        first = reverseK(node.next, count + 1)

        node.next.next = node
        node.next = successor
        if prev: prev.next = first
        return first

    index = 1
    while cur:
        if index % k == 0:
            sub_head = reverseK(rs, 0)
            prev = rs
            if index == k: head = sub_head
            rs, cur = successor, successor
        else:
            cur = cur.next
        index += 1
    return head


def print_list(head: ListNode):
    node = head
    while node:
        print(str(node.val) + '-->')
        node = node.next
    print('---end--')


if __name__ == '__main__':
    five = ListNode(5)
    four = ListNode(4, five)
    three = ListNode(3, four)
    two = ListNode(2, three)
    one = ListNode(1, two)
    # print_list(one)
    reversed_node = reverseKGroup(one, 5)
    print_list(reversed_node)




