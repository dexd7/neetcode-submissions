class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq_graph = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            prereq_graph[crs].append(pre)
        res = []
        visited = set() #because now we cant set prereq graph to empty list that might be true for courses that are never mentioned in the prereq list and they wont get added to our res array. so we need to maintain a visited set and add every course until it is not iin visited. and visited also does the cycle detection task
        cycle_detector = set()
        def canTake(course):
            if course in visited:
                return True
            if course in cycle_detector:
                return False
            cycle_detector.add(course)
            for pre in prereq_graph[course]:
                if not canTake(pre):
                    return False
            cycle_detector.remove(course)
            visited.add(course)
            res.append(course)
            return True
        for i in range(numCourses):
            if not canTake(i):
                return []
        return res