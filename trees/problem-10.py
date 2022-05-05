# Given a binary search tree, convert it into a sorted doubly-linked list by modifying the original tree nodes (do not create new nodes).

def bstToDoubly(root):
    if not root:
        return

    def dfs(node):
        nonlocal head, tail
        if not node:
            return
        dfs(node.left)
        if tail:
            tail.right = node
            node.left = tail
        else:
            head = node
        tail = node
        dfs(node.right)

    head, tail = None, None

    dfs(root)
    head.left = tail
    tail.right = head

    return head
