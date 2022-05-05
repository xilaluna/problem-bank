# Binary tree post-order-traversal

def post_order_traversal(root):
    result = []

    def traverse(root):
        if not root:
            return
        traverse(root.left)
        traverse(root.right)
        result.append(root.val)

    traverse(root)
    return result
