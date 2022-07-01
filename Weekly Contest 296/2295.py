from typing import List, Optional, Any, Dict

class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        
        index_dict = {}

        for index, num in enumerate(nums):
            index_dict[num] = index
        
        for operation in operations:

            nums[index_dict[operation[0]]] = operation[1]
            
            index_dict[operation[1]] = index_dict[operation[0]]
        
        return nums
