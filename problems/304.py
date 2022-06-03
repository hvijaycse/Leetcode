from typing import List, Optional, Any, Dict

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):

        rows = len(matrix) + 1
        columns = len(matrix[0])  + 1
        self.sum_matrix = [ 
            [0] * columns for _ in range(rows)
        ] 

        for r in range(1, rows):
            for c in range(1, columns):
                self.sum_matrix[r][c] = self.sum_matrix[r-1][c] + self.sum_matrix[r][c-1] - self.sum_matrix[r-1][c-1] + matrix[r-1][c-1]


        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        row1, row2, col1, col2 = row1+1, row2+1, col1+1, col2+1
        return self.sum_matrix[row2][col2] - self.sum_matrix[row1-1][col2] -self.sum_matrix[row2][col1-1] + self.sum_matrix[row1-1][col1-1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
