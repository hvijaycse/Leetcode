from typing import List, Optional, Any, Dict

class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        low = 0 
        high = len(nums)

        while low < high:

            if nums[low] <= nums[high-1]:
                return nums[low]
            
            low += 1
            mid = (low + high) // 2

            if nums[0] <= nums[mid]:
                low = mid
            else:
                high = mid + 1
        
        return nums[low]
    

