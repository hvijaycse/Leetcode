from typing import List, Optional, Any, Dict

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.sub= []
        self.rec(0, nums, [])

        return self.sub

    def rec(self, index: int, nums: List[int], current: List[int]):

        if index == len(nums):
            self.sub.append(list(current))
            return
        
        # including this element
        current.append(nums[index])

        self.rec(index+1, nums, current)

        # calling with including 

        current.pop()
        self.rec(index+1, nums, current)

