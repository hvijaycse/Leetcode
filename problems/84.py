from typing import List, Optional, Any, Dict


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0 

        for i in range(len(heights)):
            for j in range(i, len(heights)):

                min_height = min(heights[i:j+1])
                max_area = max(max_area , min_height * (j-i+1))
        
        return max_area