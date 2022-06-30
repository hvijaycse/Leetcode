from typing import List, Optional, Any, Dict

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        

        min_size = float('inf')
        low = 0 
        high = 0 
        total = 0

        while high < len(nums):

            while high < len(nums) and total < target:
                total += nums[high]
                high += 1

            while low <= high and total >= target:
                min_size = min(min_size, high - low )
                total -= nums[low]
                low += 1
        
        if min_size == float('inf'):
            min_size = 0

        
        return min_size

