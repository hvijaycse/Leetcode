from typing import List, Optional, Any, Dict

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:

        rows = len(matrix)
        columns = len(matrix[0])

        transpose = [
            [ matrix[r][c] for r in range(rows)] for c in range(columns)
        ]

        return transpose