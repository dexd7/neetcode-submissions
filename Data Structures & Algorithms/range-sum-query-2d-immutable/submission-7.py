class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.regionArea = [[0] * (COLS+1) for _ in range(ROWS+1)]
        for i in range(ROWS):
            prefix = 0
            for j in range(COLS):
                above = self.regionArea[i][j+1]
                prefix += matrix[i][j]
                self.regionArea[i+1][j+1] = prefix+above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1+1, col1+1, row2+1, col2+1
        main_region = self.regionArea[row2][col2]
        vertical = self.regionArea[row2][col1-1]
        horizontal = self.regionArea[row1-1][col2]
        common = self.regionArea[row1-1][col1-1]
        return main_region - vertical - horizontal + common



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)