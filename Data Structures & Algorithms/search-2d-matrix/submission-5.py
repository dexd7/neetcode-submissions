class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        bot,top = 0, ROWS-1
        while bot<=top:
            mid = (bot+top)//2
            if matrix[mid][0]>target:
                top=mid-1
            elif matrix[mid][-1]<target:
                bot=mid+1
            else:
                break #target can be in this row
        if bot>top:
            return False
        row = (bot+top)//2
        
        l = 0
        r = COLS-1
        while l<=r:
            mid = (l+r)//2
            if matrix[row][mid]>target:
                r = mid-1
            elif matrix[row][mid]<target:
                l = mid+1
            else:
                return True
        return False
        