class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        tree = {i:[] for i in range(n)}
        for node1,node2 in edges:
            tree[node1].append(node2)
            tree[node2].append(node1)
        visit = set()
        def bfs(node):
            visit.add(node)
            q = deque()
            q.append(node)
            while q:
                curr_node = q.popleft()
                for nei in tree[curr_node]:
                    if nei not in visit:
                        visit.add(nei)
                        q.append(nei)
            
        connected_components = 0
        for node in range(n):
            if node not in visit:
                bfs(node)
                connected_components+=1
        return connected_components
                


        