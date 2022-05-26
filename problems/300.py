from typing import List, Optional, Any, Dict

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        stack = []
        max_length = 0

        for num in nums:
            while stack and stack[-1] >= num:
                stack.pop()
            stack.append(num)
            max_length = max(len(stack), max_length)
        
        return max_length