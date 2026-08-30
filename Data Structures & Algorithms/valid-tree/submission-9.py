class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #RULES to make a valid tree:
        #1) All nodes of a valid tree are connected efficiently. Meaning the total number of edges in the tree must be exactly n-1
        #2) There is a way to get to every node from every node.

        #Edges == n-1
        if not len(edges) == n-1:
            return False
        
        #Now we prepare graph for connections node: list of all nodes connected to the key node
        tree = {i:[] for i in range(n)}
        for node1, node2 in edges:
            tree[node1].append(node2)
            tree[node2].append(node1)
        
        #Now we visited every connection possible for every node and in the end if our set equals all nodes, means we were able to visit all nodes from 0.
        q = deque()
        visited = set()
        q.append(0)
        visited.add(0)
        while q:
            node = q.popleft()
            for conn_node in tree[node]:
                if conn_node not in visited:
                    visited.add(conn_node)
                    q.append(conn_node)
        return True if len(visited) == n else False