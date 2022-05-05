# Binary tree level order traversal

import collections


def level_order_traversal(root):
    result = []
    queue = collections.deque()
    queue.append(root)

    while queue:
        queue_length = len(queue)
        level = []
        for i in range(queue_length):
            node = queue.popleft()
            if node:
                level.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
        if level:
            result.append(level)

    return result
