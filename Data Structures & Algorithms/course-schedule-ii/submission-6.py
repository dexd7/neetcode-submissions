class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        tree = {i:[] for i in range(numCourses)}
        cycle_detector,visit = set(), set()
        
        for crs,pre in prerequisites:
            tree[crs].append(pre)
            
        output_list = []
        def dfs(cur):
            if cur in cycle_detector:
                return False

            if cur in visit:
                return True
            cycle_detector.add(cur)
            for crs in tree[cur]:
                if not dfs(crs):
                    return False
            cycle_detector.remove(cur)
            visit.add(cur)
            output_list.append(cur)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return output_list


            


