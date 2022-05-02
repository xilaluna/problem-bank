# Given a singly-linked list, reverse the order of the list by modifying the nodes’ links.

def reverseLinkedList(head):
    prev, curr = None, head
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    return prev
