class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)
        parents = [i for i in range(N+1)]
        rank = [1] * (N+1)

        def find(n):
            p = parents[n]
            while p != parents[p]:
                parents[p] = parents[parents[p]]
                p = parents[p]
            return p

        def union(n1,n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            if rank[p1]>rank[p2]:
                parents[p2] = p1
                rank[p1]+=rank[p2]
            else:
                parents[p1] = p2
                rank[p2]+=rank[p1]
            return True

        for node1, node2 in edges:
            if not union(node1,node2):
                return [node1, node2]