class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        tree = {i: [] for i in range(numCourses)} #for storing courses that each course can take
        for crs,prereq in prerequisites:
            tree[prereq].append(crs)
        def bfs(prereq,crs):
            q = deque()
            q.append(prereq)
            visited = set()
            visited.add(prereq)
            while q:
                course = q.popleft()
                for successor in tree[course]:
                    if successor == crs:
                            return True
                    if successor not in visited:
                        q.append(successor)
                        visited.add(successor)
            return False

                        
                
        ans = []
        for crs,prereq in queries:
            ans.append(bfs(prereq,crs))
        return ans

