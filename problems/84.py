from typing import List, Optional, Any, Dict


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        '''
        monotonic stacks
        '''
        heights.append(0)
        stack = [-1]
        max_area = 0
        for index in range(len(heights)):

            while heights[index] < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = index - stack[-1] -1
                max_area = max(max_area, height*width)
            
            stack.append(index)
        return max_area