from typing import List, Optional, Any, Dict
from timeDec import timeit
from functools import lru_cache


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        self.rows = len(matrix)
        self.columns = len(matrix[0])
        self.matrix = matrix

        maxarea = 0

        for r in range(self.rows):
            for c in range(self.columns):
                maxarea = max(maxarea, self.increaseSquare(r,c, r, c))
        
        return maxarea

    @lru_cache(None)
    def increaseSquare(self, r1, c1, r2, c2):
        # print(r1,c1, r2, c2)

        if r1 == self.rows or r2 == self.rows:
            return 0

        if c1 == self.columns or c2 == self.columns:
            return 0
        
        # checking condition
        for r in range(r2, r1 +1):
            if self.matrix[r][c2] != '1':
                return 0
        
        for c in range(c1, c2 + 1):
            if self.matrix[r1][c] != '1':
                return 0
        

        return (c2 - c1 + 1) + (r1 - r2 + 1) - 1 + self.increaseSquare(r1+1, c1, r2, c2+1)
    


print(Solution().maximalSquare([["0","1"]]
))