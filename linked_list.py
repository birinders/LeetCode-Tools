class LinkedNode:
    def __init__(self, val=0, next=None, prev=None) -> None:
        self.val = val
        self.next = next
        self.prev = prev


def buildLinkedList(values, doubly=False):
    if not values:
        return LinkedNode()

    head = LinkedNode(values[0])
    prev = head
    for val in values[1:]:
        new_node = LinkedNode(val)
        if doubly:
            new_node.prev = prev
        prev.next = new_node
        prev = new_node

    return head


def convert_to_doubly(head):
    prev = None
    h1 = head
    while h1:
        h1.prev = prev
        prev = h1
        h1 = h1.next

    return head


def print_ll(head, sep=" -> "):
    default_sep = " -> "

    if hasattr(head, "prev") and sep == default_sep:
        sep = " <-> "

    ans = []
    while head:
        ans.append(head.val)
        head = head.next
    str_ans = map(str, ans)
    print(sep.join(str_ans))
    return ans


def reverse_ll(head):
    prev = None
    while head:
        actual_next = head.next
        head.next = prev
        prev = head
        head = actual_next

    return prev
