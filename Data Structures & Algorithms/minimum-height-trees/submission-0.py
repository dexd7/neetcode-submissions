class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]
        for node1, node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)
        def dfs(node, parent):
            if node == None:
                return float('inf')
            curr_height = 0
            for nei in adj[node]:
                if nei == parent:
                    continue
                curr_height = max(curr_height, 1+dfs(nei, node))
            return curr_height
        minHeight = n
        res = []
        for i in range(n):
            height = dfs(i, -1)
            if height == minHeight:
                res.append(i)
            elif height<minHeight:
                res = [i]
                minHeight = height
        return res