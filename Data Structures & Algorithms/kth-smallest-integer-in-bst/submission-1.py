# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = None
        newK = k
        def inOrderTraversal(node):
            nonlocal res
            nonlocal newK
            if not node:
                return
            inOrderTraversal(node.left)
            newK-=1
            if newK == 0:
                res = node.val
            inOrderTraversal(node.right)

                
        inOrderTraversal(root)
        return res
        
        