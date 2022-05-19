from typing import List, Optional, Any, Dict


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        rows = len(matrix)
        columns = len(matrix[0])

        dp = [
            [ None for _ in range(columns)] for _ in range(rows)
        ]

        def dfs(r: int,c: int, prev: int):
            if r < 0 or r >= rows or c < 0 or c >= columns:
                return []
            elif matrix[r][c] <= prev:
                return []
            else:
                if dp[r][c] is None:

                    neighbours = [
                        dfs(r-1, c, matrix[r][c]),
                        dfs(r, c-1, matrix[r][c]),
                        dfs(r, c+1, matrix[r][c]),
                        dfs(r+1, c, matrix[r][c])
                    ]
                    maximum = []
                    for neighbour in neighbours:
                        if len(neighbour) > len(maximum):
                            maximum = neighbour
                    dp[r][c] = [matrix[r][c]] + maximum
                        
                return dp[r][c]
        max_length = 0
        for r in range(rows):
            for c in range(columns):
                dfs(r, c, -1)
                if len(dp[r][c]) > max_length:
                    max_length = len(dp[r][c])

        return max_length
