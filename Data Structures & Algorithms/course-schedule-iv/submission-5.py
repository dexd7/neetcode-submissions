class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = {course: [] for course in range(numCourses)}
        is_prereq = [[False]*numCourses for _ in range(numCourses)]
        in_degree = [0] * numCourses
        for pre, crs in prerequisites:
            graph[pre].append(crs)
            in_degree[crs]+=1
        queue = deque([course for course in range(numCourses) if in_degree[course]==0])
        while queue:
            no_pre_course = queue.popleft()
            for course in graph[no_pre_course]:
                is_prereq[no_pre_course][course] = True
                for k in range(numCourses):
                    if is_prereq[k][no_pre_course]:
                        is_prereq[k][course] = True
                in_degree[course] -= 1
                if in_degree[course] == 0:
                    queue.append(course)
        return [is_prereq[u][v] for u,v in queries]
        