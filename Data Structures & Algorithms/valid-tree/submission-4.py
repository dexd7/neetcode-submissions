class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #All the nodes of a tree must be connected.
        #There must be a way to get to every node from each node.
        #The number of edges is equal to the number of vertices-1
        if len(edges) != n-1:
            return False
        tree = {i:[] for i in range(n)}
        #so we keep track of all the neighbours.
        for node1,node2 in edges:
            tree[node1].append(node2)
            tree[node2].append(node1)
        q = deque()
        q.append(0)
        visit = set()
        visit.add(0)
        while q:
            node = q.popleft()
            for conn_node in tree[node]:
                if conn_node not in visit:
                    visit.add(conn_node)
                    q.append(conn_node)
        return len(visit) == n

