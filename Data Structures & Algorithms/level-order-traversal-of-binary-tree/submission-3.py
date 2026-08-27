# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # if not root:
        #     return []
        # queue = deque([root])
        # levels = []
        # while queue:
        #     temp = []
        #     for _ in range(len(queue)):
        #         node = queue.popleft()
        #         temp.append(node.val)
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        #     levels.append(temp)
        # return levels

        # DFS approach  
        res = []
        def dfs(node, depth):
            if node is None:
                return None
            if len(res) == depth:
                res.append([])
            res[depth].append(node.val)
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)
        dfs(root, 0)
        return res