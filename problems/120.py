from typing import List, Optional, Any, Dict

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        self.n = len(triangle)


        for index in range(len(triangle)-2, -1, -1):

            for i in range(len(triangle[index])):
                triangle[index][i] += min(triangle[index+1][i], triangle[index+1][i+1])
        
        return triangle[0][0]