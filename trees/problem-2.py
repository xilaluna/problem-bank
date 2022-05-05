# Binary Tree Pre-order-traversal

def pre_order_traversal(root):
    result = []

    def traverse(root):
        if not root:
            return
        result.append(root.val)
        traverse(root.left)
        traverse(root.right)

    traverse(root)
    return result
