# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Non-optimal BFS
        # if not preorder or not inorder:
        #     return None

        # root = TreeNode(preorder[0])
        # mid = inorder.index(preorder[0])
        # root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])
        # root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])
        # return root

        #Optimal uses hashMap for the inorder list because that is where our solution trips up:
        #we can also avoid slizing if we use indexes
        inorder_map={val: idx for idx, val in enumerate(inorder)}
        def dfs(pre_left, pre_right, in_left, in_right):
            if pre_left>pre_right or in_left>in_right:
                return
            root_val = preorder[pre_left]
            mid = inorder_map[root_val]
            root = TreeNode(root_val)
            left_size = mid - in_left
            root.left = dfs(pre_left+1, pre_left+left_size, in_left, mid-1)
            root.right = dfs(pre_left+left_size+1, pre_right, mid+1, in_right)
            return root
        return dfs(0, len(preorder)-1, 0, len(inorder)-1)

            