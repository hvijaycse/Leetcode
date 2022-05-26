from typing import List, Optional, Any, Dict

class Solution:
    def numTilings(self, n: int) -> int:
        
        ways = [0, 1, 2, 5]

        for number in range(4, n + 1):
            way = 0 

            for i in range(1, number):
                way += ways[i] * ways[number - i]
            
            ways.append(way)
            
        return ways[n]
