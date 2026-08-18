class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        tree = {i:[] for i in range(n)}
        for node1,node2 in edges:
            tree[node1].append(node2)
            tree[node2].append(node1)
        visit = set()
        def dfs(node):
            for nei in tree[node]:
                if nei not in visit:
                    visit.add(nei)
                    dfs(nei)

            
        connected_components = 0
        for node in range(n):
            if node not in visit:
                visit.add(node)
                dfs(node)
                connected_components+=1
        return connected_components
                


        