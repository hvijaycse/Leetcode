from typing import List, Optional, Any, Dict


class Solution:

    def subsets(self, nums: List[int], lo: int, hi: int) -> List[List[int]]:
        if lo == hi:
            return [[]]
        else:
            i = lo
            while i < hi and nums[i] == nums[lo]:
                i += 1
            this_subset = [[nums[lo]]*time for time in range(1, i - lo + 1)]

            lower_subset = self.subsets(nums, lo=i, hi=hi)

            mixed_subset = []

            for item in this_subset:
                for subset in lower_subset:
                    mixed_subset.append(item + subset)

            return lower_subset + mixed_subset




    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        
        return self.subsets(nums, 0, len(nums))
