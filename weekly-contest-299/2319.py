from operator import le
from typing import List, Optional, Any, Dict

class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        
        n = len(grid) - 1
        for r in range(len(grid)):
            for c in range(len(grid[0])):

                if (r == c or r + c == n -1):
                    if grid[r][c] == 0:
                        return False
                elif grid[r][c] != 0:
                    return False
        
        return True
