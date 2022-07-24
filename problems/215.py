from typing import List, Optional, Any, Dict

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        targetIndex = len(nums) - k
        start = 0 
        end = len(nums) - 1

        while True:
            
            currIndex = self.partition(nums, start, end)

            if currIndex == targetIndex:
                break
            elif currIndex < targetIndex:
                start = currIndex + 1
            else:
                end = currIndex - 1 
            
        
        return nums[currIndex]



    def partition(self, nums: List[int], start: int, end: int):

        pivotIndex = end 

        partitonIndex = start - 1

        for index in range(start, end):

            if nums[index] <= nums[pivotIndex]:
                partitonIndex += 1
                nums[partitonIndex], nums[index] = nums[index], nums[partitonIndex]
            
        partitonIndex += 1
        nums[partitonIndex], nums[pivotIndex] = nums[pivotIndex], nums[partitonIndex]

        return partitonIndex



