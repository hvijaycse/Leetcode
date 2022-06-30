from typing import List, Optional, Any, Dict


class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        
        self.rows = len(grid)
        self.columns = len(grid[0])
        self.grid = grid

        dp = [
            [-1 for _ in range(self.columns)]
            for _ in range(self.rows)
        ]

        path = set((self.rows-1, self.columns-1))

        dp[self.rows-1][self.columns-1] = self.bfs(self.rows -1, self.columns -1, path, dp)

        return dp[self.rows-1][self.columns-1]
    
    def bfs(self, r, c, path:set, dp):

        if r == self.rows or r < 0 or c == self.columns or c < 0:
            return float('inf')
        
        if dp[r][c] != -1:
            return dp[r][c]
        
        min_val = float('inf')

        if (r-1, c) not in path:
            path.add((r-1, c))
            min_val = min(min_val, self.bfs(r-1,c, path, dp))
            path.remove((r-1,c))
        
        if (r+1,c) not in path:

            path.add((r+1, c))
            min_val = min(min_val, self.bfs(r+1,c, path, dp))
            path.remove((r+1, c))
        
        if (r, c+1) not in path:
            path.add((r, c+1))
            min_val = min(min_val, self.bfs(r,c+1, path, dp))
            path.remove((r,c+1))
        
        if (r,c-1) not in path:

            path.add((r, c-1))
            min_val = min(min_val, self.bfs(r,c-11, path, dp))
            path.remove((r,c-1))
        
        if min_val == float('inf'):
            min_val = 0 
        
        dp[r][c] = self.grid[r][c] + min_val

        return dp[r][c]        

        
        