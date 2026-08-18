# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter = 0
        def dfs(cur):
            if cur is None:
                return 0
            nonlocal maxDiameter
            left = dfs(cur.left)
            right = dfs(cur.right)
            maxDiameter = max(maxDiameter, left+right) # because we do not include the root node 
            # (to account for number of edges not number of nodes!!)
            return 1 + max(left,right)
        dfs(root)
        return maxDiameter
