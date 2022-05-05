# Given a binary tree containing numbers,
# find the maximum sum path (the path that has the largest sum of node values).
# The path may start and end at any node in the tree.

def max_sum_path(root):
    result = [root.val]

    def dfs(root):
        if not root:
            return 0

        left_max = dfs(root.left)
        right_max = dfs(root.right)

        left_max = max(left_max, 0)
        right_max = max(right_max, 0)

        result[0] = max(result[0], root.val + left_max + right_max)

        return root.val + max(left_max, right_max)

    dfs(root)
    return result
