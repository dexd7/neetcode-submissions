# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDia = float('-inf')
        def dfs(node):
            if node is None:
                return 0
            nonlocal maxDia
            right = dfs(node.left)
            left = dfs(node.right)
            maxDia = max(maxDia, left+right)
            return 1 + max(left,right)
        dfs(root)
        return maxDia