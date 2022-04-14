from typing import List, Optional, Any, Dict

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        index = 0 
        i = 0

        while i < len(nums):

            j = i 

            while j < len(nums) and nums[j] == nums[i]:
                j += 1
            
            for _ in range(min(2, j-i)):
                nums[index] = nums[i]
                index += 1
            i = j
        return index