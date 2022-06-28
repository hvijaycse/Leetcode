from typing import List, Optional, Any, Dict

class Solution:
    def countHousePlacements(self, n: int) -> int:
        mod = 10**9 + 7
        placed = [0 for _ in range(n)]
        not_placed = [0 for _ in range(n)]

        placed[-1] = 1
        not_placed[-1] = 1

        for i in range(n-2,-1,-1):
            not_placed[i] = placed[i+1] + not_placed[i+1]
            placed[i] = not_placed[i+1]
        
        total_ways = placed[0] + not_placed[0]

        total_ways *= total_ways

        return total_ways % mod
