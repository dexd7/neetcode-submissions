class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        tree = {i:[] for i in range(numCourses)}
        for crs,prereq in prerequisites:
            tree[crs].append(prereq)
        #to detect course cycles we maintain a set.
        visit = set()
        def isValid(course):
            if course in visit: #cycle detected
                return False
            #there have to be some courses with empty prereqs to maintain cycle.
            if tree[course] == []:
                return True
            visit.add(course)
            for precrs in tree[course]:
                if not isValid(precrs):
                    return False
            visit.remove(course)
            tree[crs] = []
            return True

        for i in range(numCourses):
            if not isValid(i):
                return False
        return True