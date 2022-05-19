from typing import List, Optional, Any, Dict


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        length = len(grid)
        level = 1
        for r in range(length):
            for c in range(length):
                if grid[r][c] == 0:
                    grid[r][c] = -1


        queue = []

        if grid[0][0] == -1:
            grid[0][0] = 1
            queue.append((0,0,1))

        while queue:
            r,c,w  = queue.pop(0)
            
            for row in range(max(r-1, 0), min(r+2, length)):
                for col in range(max(c-1, 0), min(c+2, length)):
                    if grid[row][col] == -1:
                        grid[row][col] = w + 1
                        queue.append((row, col, w + 1))
        
        return grid[-1][-1]


