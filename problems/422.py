from typing import List, Optional, Any, Dict
from timeDec import timeit


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        duplicates = []

        for num in nums:

            index = abs(num) - 1

            if nums[index] < 0:
                duplicates.append(abs(num))
            
            nums[index] = -1 * abs(nums[index])
        
        return duplicates