class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        tree = {node: [] for node in range(n)}
        for node1,node2 in edges:
            tree[node1].append(node2)
            tree[node2].append(node1)
        visited = set()
        def dfs(node, parent):
            if node in visited: #Cycle detected node visited again
                return False 
            visited.add(node)
            for node2 in tree[node]:
                if node2 == parent:
                    continue
                if not dfs(node2, node):
                    return False
            return True
        if not dfs(0, -1):
            return False
        return len(visited) == n