from typing import List, Optional, Any, Dict

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        rows = len(matrix)
        columns = len(matrix[0])

        zeroRows = set()
        zeroColumns = set()

        for r in range(rows):
            for c in range(columns):
                if matrix[r][c] == 0:
                    zeroRows.add(r)
                    zeroColumns.add(c)
        
        for row in zeroRows:
            for c in range(columns):
                matrix[row][c] = 0
        
        for column in zeroColumns:
            for r in range(rows):
                matrix[r][column] = 0
        
