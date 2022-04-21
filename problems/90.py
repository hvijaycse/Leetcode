from typing import List, Optional, Any, Dict




class Solution:

    def subsets(self, nums: List[int], lo: int, hi: int) -> List[List[int]]:
        if lo == hi:
            return [[]]
        else:
            i = lo
            while i < hi and nums[i] == nums[lo]:
                # Getting the index where nums[i] != num[lo]
                i += 1
            
            # Subset due to repeated numbers
            # for eg:
            #   "1" : ["1"]
            #   "1","1": ["1"],["1", "1"]

            number_subet = [[nums[lo]]*time for time in range(1, i - lo + 1)]

            # Subset of remaining numbers
            reamining_subset = self.subsets(nums, lo=i, hi=hi)

            total_subset = []

            # Creating list of all the subsets.
            for item in number_subet:
                for subset in reamining_subset:
                    total_subset.append(item + subset)

            return reamining_subset + total_subset




    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        return self.subsets(nums, 0, len(nums))
