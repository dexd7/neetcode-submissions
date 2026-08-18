# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, maximum):
            if root is None:
                return 0
            if root.val>=maximum:
                res = 1
            else:
                res = 0
            maximum = max(maximum, root.val)
            return res + dfs(root.left, maximum) + dfs(root.right, maximum)
        return dfs(root, root.val)
