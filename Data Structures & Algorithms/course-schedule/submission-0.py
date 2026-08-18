class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        tree = {i:[] for i in range(numCourses)}
        for i in range(len(prerequisites)):
            tree[prerequisites[i][0]].append(prerequisites[i][1])
        visited = set() #track of all courses we have seen so far
        def dfs(course):
            if course in visited:
                return False
            if tree[course] == []:
                return True
            visited.add(course)
            for pre in tree[course]:
                if not dfs(pre):
                    return False
            visited.remove(course)
            tree[course] = []
            return True
        for crs, prerequisite in prerequisites:
            if not dfs(crs):
                return False
        return True


            