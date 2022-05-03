# Rotate a given singly-linked list counter-clockwise by k nodes, where k is a given integer.

def rotateList(head, k):
    length, tail = 1, head
    while tail.next:
        tail = tail.next
        length += 1

    k = k % length
    if k == 0:
        return head

    current = head
    for i in range(length - k - 1):
        current = current.next
    newHead = current.next
    current.next = None
    tail.next = head

    return newHead
