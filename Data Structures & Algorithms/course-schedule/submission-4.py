class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq_graph = {course: [] for course in range(numCourses)}
        for crs, pre in prerequisites:
            prereq_graph[crs].append(pre)
        visiting = set()
        def dfs(course):
            if course in visiting:
                return False
            if len(prereq_graph[course]) == 0:
                return True
            visiting.add(course)
            for pre in prereq_graph[course]:
                if not dfs(pre):
                    return False
            visiting.remove(course)
            prereq_graph[course] = []
            return True


        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
