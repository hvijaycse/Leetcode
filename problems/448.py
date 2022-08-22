from typing import List, Optional, Any, Dict
from timeDec import timeit

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        

        for num in nums:
            index = abs(num) - 1
            nums[index] = -abs(nums[index])
        
        ans = []

        for index, num in enumerate(nums):

            if num >0 :
                ans.append(index + 1)
        
        return ans