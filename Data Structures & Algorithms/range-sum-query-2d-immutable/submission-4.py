class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.sumMap = [[] for _ in range(len(matrix))]
        for row in range(len(matrix)):
            currSum = 0
            for col in range(len(matrix[0])):
                currSum+=matrix[row][col]
                self.sumMap[row].append(currSum)


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = 0
        for r in range(row1, row2+1):
            if col1>0:
                ans +=self.sumMap[r][col2]-self.sumMap[r][col1-1]
            else:
                ans+=self.sumMap[r][col2]
        return ans


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)