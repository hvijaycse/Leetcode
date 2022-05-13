from operator import le
from typing import List, Optional, Any, Dict


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        total_permutaiton = []
        self.permutations(total_permutaiton, nums)

        return total_permutaiton

    
    def permutations(self, total_permutations: List[List[int]], nums: List[int]):
        if len(nums) == 1:
            total_permutations.append(nums)
        else:
            index = 0
            while index < len(nums):
                current = nums[index]
                temp_nums = list(nums)
                temp_nums.pop(index)
                current_permutations = []

                self.permutations(current_permutations, temp_nums)
                
                for permutations in current_permutations:
                    total_permutations.append( [current] + permutations )
                
                current_index = index
                while index < len(nums) and nums[index] == nums[current_index]:
                    index += 1
            
