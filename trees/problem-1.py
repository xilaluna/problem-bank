# Binary Tree In-order-traversal


def inOrderTraversalRecursive(root):
    result = []

    def traverse(root):
        if not root:
            return
        traverse(root.left)
        result.append(root.val)
        traverse(root.right)

    traverse(root)
    return result
