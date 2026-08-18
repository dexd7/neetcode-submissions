class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        map_courses = {i:[] for i in range(numCourses)}
        for crs,pre in prerequisites:
            map_courses[crs].append(pre)
        output = []
        cycle = set()
        visit = set()
        def dfs(course):
            if course in cycle:
                return False
            if course in visit:
                return True
            cycle.add(course)
            for prereq in map_courses[course]:
                if not dfs(prereq):
                    return False
            cycle.remove(course)
            visit.add(course)
            output.append(course)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return output