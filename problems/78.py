from typing import List, Optional, Any, Dict

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        if len(nums) == 0:
            return [[]]
        else:
            smaller_set = self.subsets(nums[1:])
            # print(smaller_set, [nums[0]])

            return smaller_set + [[nums[0]] + subset for subset in smaller_set]


# print(Solution().subsets([1,2,3]))