from typing import List, Optional, Any, Dict

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        start = 0 
        end = len(nums)

        while start < end:

            mid = (start + end) // 2

            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                start = mid+1
            else:
                end = mid
        
        return -1