class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        tree = {node: [] for node in range(n)}
        for node1,node2 in edges:
            tree[node1].append(node2)
            tree[node2].append(node1)
        visited = set()
        q = deque()
        q.append(0)
        visited.add(0)
        while q:
            node = q.popleft()
            for nei in tree[node]:
                if nei not in visited:
                    visited.add(nei)
                    q.append(nei)
        return len(visited) == n