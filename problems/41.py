from typing import List, Optional, Any, Dict
from timeDec import timeit

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        

        for index in range(len(nums)):

            if nums[index] <= 0 :
                nums[index] = len(nums) + 2
        
        for index in range(len(nums)):

            if abs(nums[index]) > len(nums):
                continue

            updateIndex = abs(nums[index]) - 1
            nums[updateIndex] = - abs(nums[updateIndex])
        

        index = 0

        while index < len(nums)  and nums[index] < 0:
            index += 1
        
        return index + 1
