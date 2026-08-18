class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        adj = [[] for _ in range(n)]
        for node1, node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)
        leaves = deque()
        edge_count = {}
        for node in range(n):
            if len(adj[node]) == 1:
                leaves.append(node)
            edge_count[node] = len(adj[node])
        while leaves:
            if n<=2:
                return list(leaves)
            for _ in range(len(leaves)):
                curr = leaves.popleft()
                n-=1
                for nei in adj[curr]:
                    edge_count[nei] -= 1
                    if edge_count[nei] == 1:
                        leaves.append(nei)
                    

