# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val
        def dfs(root):
            nonlocal res
            if root is None:
                return 0
            left_height = dfs(root.left)
            right_height = dfs(root.right)
            max_in_left_tree = max(left_height, 0)
            max_in_right_tree = max(right_height, 0)
            res = max(res, root.val + max_in_left_tree + max_in_right_tree)
            return root.val + max(max_in_left_tree, max_in_right_tree)
        dfs(root)
        return res