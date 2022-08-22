from typing import List, Optional, Any, Dict
from timeDec import timeit



class Solution:
    def minOperations(self, nums: List[int]) -> int:

        oldSum = sum(nums)

        for index in range(1, len(nums)):

            if nums[index] <= nums[index-1]:
                nums[index] = nums[index-1] + 1
        
        newSum = sum(nums)

        return newSum - oldSum
