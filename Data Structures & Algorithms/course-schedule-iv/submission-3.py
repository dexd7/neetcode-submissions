class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        tree = {i: [] for i in range(numCourses)}
        for crs,pre in prerequisites:
            tree[crs].append(pre)
        def dfs(course, requisite, visited):
            if course in visited:
                return False
            if course == requisite:
                return True
            visited.add(course)
            for pre in tree[course]:
                if dfs(pre,requisite, visited):
                    return True
            return False
        output = []
        for course, prereq in queries:
            output.append(dfs(course, prereq, set()))
        return output