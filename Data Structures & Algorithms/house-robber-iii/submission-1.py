# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # we return [maxRoot, maxWithoutRoot]
        def dfs(node):
            if node is None:
                return [0, 0]
            left_pair = dfs(node.left)
            right_pair = dfs(node.right)
            maxRoot = node.val + left_pair[1] + right_pair[1]
            maxWithoutRoot = max(left_pair) + max(right_pair)
            return [maxRoot, maxWithoutRoot]
        return max(dfs(root))        