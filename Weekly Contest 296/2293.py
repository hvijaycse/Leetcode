from typing import List, Optional, Any, Dict

class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        
        n = len(nums)

        while n > 1:

            n = n // 2
            for i in range(n):
                if i %2 == 0 :
                    nums[i] = min(nums[2*i], nums[2*i + 1])
                else:
                    nums[i] = max(nums[2*i], nums[2*i + 1])
        
        return nums[0]

