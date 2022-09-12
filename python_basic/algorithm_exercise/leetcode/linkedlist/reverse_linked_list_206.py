class ListNode:
    def __init__(self, val:int, next=None):
        self.val = val
        self.next = next


def reverse_list(head: ListNode) -> ListNode:
    cur, prev = head, None
    while cur:
        cur.next, prev, cur = prev, cur, cur.next
    return prev


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
    #print_list(one)
    reversed_node = reverse_list(one)
    print_list(reversed_node)
