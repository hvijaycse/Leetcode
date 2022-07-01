from typing import List, Optional, Any, Dict

class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        
        nums.sort()

        index = 0 
        partitions = 0
        
        while index < len(nums):

            target = nums[index] + k

            last_index = self.binary(nums, index + 1, len(nums), target)

            partitions += 1
            index = last_index + 1
        
        return partitions
    
    def binary(self,nums, low, high , target):

        last_index = -1

        while low < high:

            mid = low + (high - low) // 2

            if nums[mid] == target:
                last_index = mid
                low = mid + 1
            
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid
        
        if last_index == -1:
            return low - 1
        else:
            return last_index

