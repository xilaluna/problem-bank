# Given a binary search tree containing integers and a target integer,
# come up with an efficient way to locate two nodes in the tree whose sum is equal to the target value.

def two_sum_bst(root, k):
    lookup = set()

    def dfs(node):
        if not node:
            return False

        y = k - node.val

        if y in lookup:
            return True
        else:
            lookup.add(node.val)
        return dfs(node.left) or dfs(node.right)

    return dfs(root)
