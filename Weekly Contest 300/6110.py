from typing import List, Optional, Any, Dict

class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        '''
        Can be more optimized in term of coding
        '''

        self.rows = len(grid)
        self.columns = len(grid[0])
        self.grid = grid

        matrix = [
            [1 for _ in range(self.columns)]
            for _ in range(self.rows)
        ]

        visited = set()
        total_ways = 0 

        for i in range(self.rows):
            for j in range(self.columns):
                if (i, j) not in visited:
                    self.dfs(i, j, visited, matrix, -1)
                total_ways += matrix[i][j]

        return total_ways % 1000000007      


    def dfs(self, row, column, visited, matrix, last_value):
         
        if row < 0 or row >= self.rows or column < 0 or column >= self.columns:
            return 0
        
        if self.grid[row][column] <= last_value:
            return 0 

        if (row, column) in visited:
            return matrix[row][column]
        
        matrix[row][column] += self.dfs(row+1,column, visited, matrix, self.grid[row][column])
        matrix[row][column] += self.dfs(row-1,column, visited, matrix, self.grid[row][column])
        matrix[row][column] += self.dfs(row,column+1, visited, matrix, self.grid[row][column])
        matrix[row][column] += self.dfs(row,column-1, visited, matrix, self.grid[row][column])

        visited.add((row, column))

        return matrix[row][column]

