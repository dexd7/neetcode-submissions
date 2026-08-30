class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        tree = {node: [] for node in range(n)}
        for node1, node2 in edges:
            tree[node1].append(node2)
            tree[node2].append(node1)
        visited = set()
        def dfs(node):
            for nei in tree[node]:
                if nei not in visited:
                    visited.add(nei)
                    dfs(nei)
            return
        connected_components = 0
        for node in range(n):
            if node not in visited:
                visited.add(node)
                dfs(node)
                connected_components +=1
        return connected_components