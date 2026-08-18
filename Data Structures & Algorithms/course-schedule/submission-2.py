class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        map_courses = {i:[] for i in range(numCourses)}
        for crs,pre_req in prerequisites:
            map_courses[crs].append(pre_req)
        cycles = set()
        def dfs(course):
            if course in cycles:
                return False
            if map_courses[course] == []:
                return True
            cycles.add(course)
            for prereq in map_courses[course]:
                if not dfs(prereq):
                    return False
            cycles.remove(course)
            map_courses[course] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
