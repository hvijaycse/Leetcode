from typing import List, Optional, Any, Dict

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:

        indexes = {}
        lastIndex = -1
        maxsum = 0
        current = 0 
        for index in range(len(nums)):
            current += nums[index]

            if nums[index] in indexes:
                toIndex = max(lastIndex, indexes[nums[index]])

                for j in range(lastIndex+1, toIndex + 1):
                    current -= nums[j]
                lastIndex = toIndex
            
            maxsum = max(maxsum, current)
            indexes[nums[index]] = index
        
        return maxsum
            
