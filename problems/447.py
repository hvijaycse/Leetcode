from typing import List, Optional, Any, Dict


class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        
        total = 0 
        length = len(nums)

        for i in range(length-1):
            for j in range(i+1, length):
                xor = nums[i] ^ nums[j]

                while xor:
                    xor &= (xor-1)
                    total += 1
        
        return total