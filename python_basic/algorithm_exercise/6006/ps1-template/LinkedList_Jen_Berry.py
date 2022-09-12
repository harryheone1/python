
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# None
# o
# o -> o
# o -> o -> o
# o -> o -> o -> o

def reorder_students(L):
    head = L.head
    if not head: return L

    reverse_root = None
    slow = fast = head
    # 跳的两种方法之一，跳之前检查
    while True:
        if slow.next and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        else:
            reverse_root = slow
            break

    if reverse_root and reverse_root.next:
        reverse_start = reverse_root.next()
        reverse_root.next = reverse_linkedlist(reverse_start)

    return L

def reverse_linkedlist(head: Node) -> Node:
    if not head.next:
        return head

    reverse_head = reverse_linkedlist(head.next)
    head.next.next = head
    head.next = None
    return reverse_head

