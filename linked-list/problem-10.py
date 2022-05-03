# Given a singly-linked list and an integer k, find the value in the kth-to-last node.
from multiprocessing import dummy


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthNode(head, n):
    dummy = ListNode(0, head)
    left, right = dummy, head

    while n > 0 and right:
        right = right.next
        n -= 1

    while right:
        left = left.next
        right = right.next

    left.next = left.next.next

    return dummy.next
