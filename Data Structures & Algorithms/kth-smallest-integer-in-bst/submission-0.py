# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        def inOrderTraversal(node):
            nonlocal res
            if node is None:
                return 
            inOrderTraversal(node.left)
            res.append(node.val)
            inOrderTraversal(node.right)
            return 
        
        inOrderTraversal(root)
        return res[k-1]
        
        