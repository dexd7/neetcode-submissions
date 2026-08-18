# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        return (self.treesEqual(root,subRoot) or
                self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))
    def treesEqual(self, tree1, tree2):
        if not tree1 and not tree2:
            return True
        if not tree1 or not tree2:
            return False
        return (tree1.val == tree2.val and 
                self.treesEqual(tree1.left, tree2.left) 
                and self.treesEqual(tree1.right, tree2.right))
            
