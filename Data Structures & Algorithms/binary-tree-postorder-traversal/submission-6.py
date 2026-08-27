# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # res = []
        # def dfs(node):
        #     if not node:
        #         return
        #     dfs(node.left)
        #     dfs(node.right)
        #     res.append(node.val)
        # dfs(root)
        # return res
        #Iterative approach
        cur = root
        stack = []
        res = []
        while cur or stack:
            if cur:
                res.append(cur.val)
                stack.append(cur.left)
                cur = cur.right
            else:
                cur = stack.pop()
        return list(res[::-1])