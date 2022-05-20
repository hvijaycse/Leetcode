from typing import List, Optional, Any, Dict


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        rows = len(obstacleGrid)
        columns = len(obstacleGrid[0])

        prev = 1
        for c in range(columns):
            if obstacleGrid[0][c] == 1:
                prev = -1
            obstacleGrid[0][c] = prev
        
        prev = obstacleGrid[0][0]

        for r in range(1,rows):
            if obstacleGrid[r][0] == 1:
                prev = -1
            obstacleGrid[r][0] = prev
        
        for r in range(1, rows):
            for c in range(1, columns):
                if obstacleGrid[r][c] == 1:
                    obstacleGrid[r][c] = -1
                else:
                    up = max(0, obstacleGrid[r-1][c])
                    left = max(0, obstacleGrid[r][c-1])

                    obstacleGrid[r][c] = up + left
        
        for row in obstacleGrid:
            print(row)
        
        return max(0, obstacleGrid[-1][-1])