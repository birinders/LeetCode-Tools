from typing import Iterable
from typing import Final

null: Final = None


class ListNode:
    def __init__(self, val=0, next=None, prev=None) -> None:
        self.val = val
        self.next = next
        if prev:
            self.prev = prev


def buildLinkedList(values: Iterable, doubly: bool = False, get_tail: bool = False):
    """
    values: A 1d iterable
    doubly: bool- Set true if you want the ll to be doubly linked
    get_tail: returns the tail of the ll in the tuple (head, tail)

    Return None if "values" is empty.

    """
    if not values:
        return None

    head = ListNode(values[0])
    prev = head
    for val in values[1:]:
        new_node = ListNode(val)
        if doubly:
            new_node.prev = prev
        prev.next = new_node
        prev = new_node

    if get_tail:
        return head, new_node
    return head


def convert_to_doubly(head: ListNode) -> ListNode:
    """
    Returns the head of the linked list after linking it doubly
    """
    prev = None
    h1 = head
    while h1:
        h1.prev = prev
        prev = h1
        h1 = h1.next

    return head


def print_ll(head: ListNode, sep: str = " -> ") -> None:
    """
    Prints the linked list with the provided seperator. If no seperator is provided, " -> " is used by default.

    Note: Head may be some other Linked List object as long as it uses the .next pointer for the next node
    """
    default_sep = " -> "

    if hasattr(head, "prev") and sep == default_sep:
        sep = " <-> "

    ans = []
    while head:
        ans.append(head.val)
        head = head.next
    str_ans = map(str, ans)
    print(sep.join(str_ans))
    # return ans


def get_ll_elems(head: ListNode) -> list[object]:
    """
    Returns a list of all the elements inside the Linked List.

    Note: Head may be some other Linked List object as long as it uses the .next pointer for the next node
    """
    ret = []
    while head:
        ret.append(head.val)
        head = head.next
    return ret


def get_len(head: ListNode) -> int:
    """
    head: An object of ListNode type

    Note: Head may be some other Linked List object as long as it uses the .next pointer for the next node

    Warning: Do not pass in any linked list with a loop in it, or the function goes into infinite execution
    """
    ret = 0
    while head:
        ret += 1
        head = head.next
    return ret


def get_tail(head: ListNode) -> ListNode:
    """
    head: An object of ListNode type

    Note: Head may be some other Linked List object as long as it uses .next and .prev pointers for the next and prev node

    Warning: Do not pass in any linked list with a loop in it, or the function goes into infinite execution
    """
    while head.next:
        head = head.next
    return head


def reverse_ll(head: ListNode, get_tail: bool = False) -> ListNode:
    """
    head: An object of ListNode type
    get_tail: Set true to get the tail of the reversed list as well in the tuple (head, tail)

    Note: Head may be some other Linked List object as long as it uses .next and .prev pointers for the next and prev node

    Warning: Do not pass in any linked list with a loop in it, as that will result in undefined behaviour
    """
    # Check if the linked list is linked doubly

    final_tail = head

    prev = None
    while head:
        # Store the actual next aside
        actual_next = head.next

        # Change the next node to whatever the previous node is
        head.next = prev

        # If the linked list is doubly linked, set the prev node to actual_next
        if hasattr(head, "prev"):
            head.prev = actual_next

        prev = head
        head = actual_next

    if get_tail:
        return prev, final_tail
    return prev
