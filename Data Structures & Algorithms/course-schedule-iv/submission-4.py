class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        tree = {i: [] for i in range(numCourses)}
        for crs,pre in prerequisites:
            tree[crs].append(pre)
        def bfs(crs, pre):
            q = deque()
            visited = set()
            q.append(crs)
            visited.add(crs)
            while q:
                curr_course = q.popleft()
                for prereq in tree[curr_course]:
                    if pre == prereq:
                        return True
                    if prereq not in visited:
                        q.append(prereq)
                        visited.add(prereq)
            return False
                     
        output = []
        for course, prereq in queries:
            output.append(bfs(course, prereq))
        return output