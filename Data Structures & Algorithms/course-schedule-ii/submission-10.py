class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq_map = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            prereq_map[crs].append(pre)
        cycle_detector = set()
        visited = set()
        output = []
        def dfs(course):
            if course in cycle_detector:
                return False
            if course in visited:
                return True
            cycle_detector.add(course)
            for pre in prereq_map[course]:
                if not dfs(pre):
                    return False
            cycle_detector.remove(course)
            visited.add(course)
            output.append(course)
            return True

        for num in range(numCourses):
            if not dfs(num):
                return []
        return output