# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        last_element_only = []
        q = deque([root])
        while q:
            temp = 0
            for i in range(len(q)):
                node = q.popleft()
                temp = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            last_element_only.append(temp)
        return last_element_only