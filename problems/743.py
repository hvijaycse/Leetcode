from typing import List, Optional, Any, Dict


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        matrix = [[-1 for _ in range(n+1)] for _ in range(n+1)]

        for time in times:
            matrix[time[0]][time[1]] = time[2] 
        
        time_taken = {
            i: float('inf') for i in range(1, n+1)
        }

        time_taken[k] = 0 

        def dfs(r:int, prev_weight):

            for c in range(1, n+1):
                if matrix[r][c] != -1:
                    if prev_weight + matrix[r][c] < time_taken[c]:
                        time_taken[c] = prev_weight + matrix[r][c]
                        dfs(c, time_taken[c])

        dfs(k, 0)

        
        maximum = max(time_taken.values())
        
        return maximum if maximum != float('inf') else -1
            