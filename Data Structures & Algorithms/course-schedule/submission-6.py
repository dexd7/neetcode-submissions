class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq_graph = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            prereq_graph[crs].append(pre)
        cycle_detector = set()
        def canTake(course):
            if prereq_graph[course] == []:
                return True
            if course in cycle_detector:
                return False
            cycle_detector.add(course)
            for pre in prereq_graph[course]:
                if not canTake(pre):
                    return False
            cycle_detector.remove(course)
            prereq_graph[course] = []
            return True
        for i in range(numCourses):
            if not canTake(i):
                return False
        return True