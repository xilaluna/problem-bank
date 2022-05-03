# Given an array of k singly-linked lists, each of whose values are in sorted order,
# combine all nodes (do not create new nodes) into one singly-linked list with all values in order.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeList(l1, l2):
    dummy = ListNode()
    tail = dummy
    while l1 and l2:
        if l1.val < l2.val:
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    if l1:
        tail.next = l1
    if l2:
        tail.next = l2
    return tail


def mergeLists(lists):
    if not lists or len(lists) == 0:
        return None
    while len(lists):
        listsArray = []
        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i + 1] if (i + 1) < len(lists) else None
            listsArray.append(mergeList(l1, l2))
        lists = listsArray

    return lists[0]
