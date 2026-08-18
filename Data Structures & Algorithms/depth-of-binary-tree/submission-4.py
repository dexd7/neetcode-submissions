# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        stack = [(root,1)]
        maxHeight = 0
        while stack:
            cur,height = stack.pop()
            maxHeight = max(height, maxHeight)
            if cur.left:
                stack.append((cur.left,height+1))
            if cur.right:
                stack.append((cur.right,height+1))

        return maxHeight