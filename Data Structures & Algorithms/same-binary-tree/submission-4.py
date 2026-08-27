# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if p is None and q is None:
        #     return True
        # if  p is None or q is None or p.val != q.val:
        #     return False
        # return self.isSameTree(p.left,q.left) and self.isSameTree(p.right, q.right)

        #Iterative approach now:
        stack = [(p,q)]
        while stack:
            node_p, node_q = stack.pop()
            if node_p is None and node_q is None:
                continue
            if not node_p or not node_q or node_p.val != node_q.val:
                return False
            stack.append((node_p.left, node_q.left))
            stack.append((node_p.right, node_q.right))
        return True