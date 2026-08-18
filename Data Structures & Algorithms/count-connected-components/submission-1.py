class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        tree = {i:[] for i in range(n)}
        for node1,node2 in edges:
            tree[node1].append(node2)
            tree[node2].append(node1)
        visit = [False] * n
        def bfs(node):
            visit[node] = True
            q = deque()
            q.append(node)
            while q:
                curr_node = q.popleft()
                for nei in tree[curr_node]:
                    if not visit[nei]:
                        visit[nei] = True
                        q.append(nei)
            
        connected_components = 0
        for node in range(n):
            if not visit[node]:
                bfs(node)
                connected_components+=1
        return connected_components
                


        