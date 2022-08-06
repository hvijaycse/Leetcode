from typing import List, Optional, Any, Dict
from timeDec import timeit


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        triangle = [1 for _ in range(rowIndex + 1)]

        for row in range(1, rowIndex):

            temp_triangle = list(triangle)

            for index in range(1, row+1):
                temp_triangle[index] += triangle[index-1]
            
            triangle = temp_triangle
        
        return triangle