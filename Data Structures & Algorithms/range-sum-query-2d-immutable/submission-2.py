class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix = [[] for _ in range(len(matrix))]
        for i in range(len(matrix)):
            curr_sum = 0
            for j in range(len(matrix[0])):
                curr_sum += matrix[i][j]
                self.prefix[i].append(curr_sum)



    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = 0
        for i in range(row1,row2+1):
            if col1>0:
                ans+=self.prefix[i][col2] - self.prefix[i][col1-1]
            else:
                ans+=self.prefix[i][col2]
        return ans
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)