# Given a binary search tree, reverse the order of its values by modifying the nodes’ links.

def invert_bin_tree(root):
    def invert(root):
        if not root:
            return None
        temp = root.left
        root.left = root.right
        root.right = temp

        invert(root.left)
        invert(root.right)

    invert(root)
    return root
