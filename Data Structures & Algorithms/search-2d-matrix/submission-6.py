class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix)-1
        candidate_row = float('inf')
        while l<=r:
            mid = l+(r-l)//2
            if matrix[mid][-1]<target:
                l = mid+1
            elif matrix[mid][0]>target:
                r = mid-1
            else:
                candidate_row = mid
                break
        if candidate_row == float('inf'):
            return False
       
        else:
            candidate_row = matrix[candidate_row]
            l = 0
            r = len(matrix[0])-1
            while l<=r:
                mid = l+(r-l)//2
                if candidate_row[mid]<target:
                    l = mid+1
                elif candidate_row[mid]>target:
                    r = mid-1
                else:
                    return True
            return False