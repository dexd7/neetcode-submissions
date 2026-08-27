# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #RECURSIVE APPROACH FIRST
        # res = []
        # def dfs(node, depth):
        #     if node is None:
        #         return None
        #     if depth == len(res):
        #         res.append(node.val)
        #     dfs(node.right, depth+1)
        #     dfs(node.left, depth+1)
        # dfs(root, 0)
        # return res
        #Iterative approach now
        if root is None:
            return []
        queue = deque([root])
        res = []
        while queue:
            temp = None
            for _ in range(len(queue)):
                node = queue.popleft()
                temp = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(temp)
        return res