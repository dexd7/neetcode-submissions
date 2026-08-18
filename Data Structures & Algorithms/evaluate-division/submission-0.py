class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        for i, eq in enumerate(equations):
            u, v = eq
            adj[u].append([values[i], v])
            adj[v].append([1/values[i],u]) # keeping inverse for reverse direction (denom->numerator)
        
        def bfs(src, target):
            if src not in adj or target not in adj:
                return -1
            visited = set()
            q = deque()
            q.append((src, 1))
            visited.add(src)
            while q:
                var, running = q.popleft()
                if var == target:
                    return running
                for value, nei in adj[var]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append((nei, running*value))
            return -1

        return [bfs(num,denom) for num, denom in queries]
        