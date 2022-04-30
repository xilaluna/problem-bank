# Given a single-linked list, find the middle value in the list.

def tortoiseAndHare(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
