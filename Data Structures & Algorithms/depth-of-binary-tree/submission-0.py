# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = deque()
        maxDepth = 0
        if root is None:
            return 0
        q.append((root,1))
        while q:
            node,depth = q.pop()
            maxDepth = max(maxDepth, depth)
            if node.left:
                q.append((node.left, depth+1))
            if node.right:
                q.append((node.right, depth+1))
        return maxDepth