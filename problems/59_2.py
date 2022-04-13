from typing import List, Optional, Any, Dict


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        grid = [[0] * n for _ in range(n)]
        index = -1
        original_n = n
        num = 0
        while n>0:

            for _ in range(n):
                index += 1
                num += 1
                grid[index // original_n][index % original_n] =num
            
            for _ in range(n-1):
                index += original_n
                num += 1
                grid[index // original_n][index % original_n] = num
            
            for _ in range(n-1):
                index -= 1
                num += 1
                grid[index // original_n][index % original_n] = num
            
            for _ in range(n-2):
                index -= original_n
                num += 1
                grid[index // original_n][index % original_n] = num
            
            n -= 2
        
        return grid