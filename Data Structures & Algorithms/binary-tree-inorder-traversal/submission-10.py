# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Recursive approach
        # ans = []
        # def dfs(node):
        #     if node is None:
        #         return
        #     dfs(node.left)
        #     ans.append(node.val)
        #     dfs(node.right)
        # dfs(root)
        # return ans
        # Iterative approach
        stack = []
        res = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        return res