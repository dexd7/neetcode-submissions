class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        tree = {i:[] for i in range(n)}
        if len(edges) != n-1:
            return False
        for node1,node2 in edges:
            tree[node1].append(node2)
            tree[node2].append(node1)
        q = deque()
        q.append(0)
        visit = set()
        visit.add(0)
        while q:
            node = q.popleft()
            for nei in tree[node]:
                if nei not in visit:
                    q.append(nei)
                    visit.add(nei)
        return len(visit) == n
            