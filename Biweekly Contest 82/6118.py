from functools import total_ordering
from re import L
from typing import List, Optional, Any, Dict

class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        
        absolute = [ abs( nums1[i] - nums2[i]) for i in range(len(nums1))]

        total = sum(absolute)

        operation = k1 + k2

        if total <= operation:
            return 0
        
        absolute.sort()

        diff = [0 for _ in range(len(nums1))]

        for i in range(1, len(nums1)):
            diff[i] = absolute[i] - absolute[i-1]
            

        total = 0 

        for num in absolute:
            total += num * num

        return total

 