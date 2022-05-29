from typing import List, Optional, Any, Dict

class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n = len(nums)
        optimalSum = n*(n+1)//2 
        totalSum = sum(nums)

        return optimalSum - totalSum
