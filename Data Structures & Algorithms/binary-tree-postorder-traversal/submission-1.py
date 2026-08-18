# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def postorder(cur):
            if cur is None:
                return 
            res.append(cur.val)
            postorder(cur.right)
            postorder(cur.left)
        postorder(root)
        return res[::-1]
