# Given a singly-linked list, rearrange the nodes by interleaving the first half of the linked list with the second half.

def rearrangeLinkedList(head):
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    second = slow.next
    prev = slow.next = None

    while second:
        temp = second.next
        second.next = prev
        prev = second
        second = temp

    first, second = head, prev

    while second:
        temp1, temp2 = first.next, second.next
        first.next = second
        second.next = temp1
        first, second = temp1, temp2
