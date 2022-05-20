from typing import List, Optional, Any, Dict

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        columns = len(grid[0])

        Visited = {}

        start_r = 0 
        start_c = 0
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == -1:
                    continue
                Visited[(r,c)] = False

                if grid[r][c] == 1:
                    start_r = r
                    start_c = c
        

        def backtracking(r, c, ways)-> int:

            if r < 0 or r >= rows or c < 0 or c >= columns:
                return 
            elif grid[r][c] == -1 or Visited[(r,c)]:
                return 

            Visited[(r,c)] = True

            if grid[r][c] == 2:
                if all(Visited.values()):
                    ways[0] += 1
            else:
                backtracking(r+1, c, ways)
                backtracking(r-1, c, ways)
                backtracking(r, c+1, ways)
                backtracking(r, c-1, ways)

            Visited[(r,c)] = False

            return


        ways = [0]

        backtracking(start_r, start_c, ways)

        return ways[0]