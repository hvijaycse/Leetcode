from typing import List, Optional, Any, Dict

class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        
        n = len(nums1)

        nums1_sum = sum(nums1)
        nums2_sum = sum(nums2)

        nums1_sum_max = nums1_sum
        nums2_sum_max = nums2_sum

        nums1.insert(0,0)
        nums2.insert(0,0)
        for i in range(1, n):
            nums1[i] += nums1[i-1]
            nums2[i] += nums2[i-1]
        
        

        for i in range(1,n):
            for j in range(i, n):

                nums1_sum_max = max( nums1_sum_max,  nums1_sum - (nums1[j] - nums1[i-1]) + nums2[j] - nums2[i-1])
                nums2_sum_max = max( nums2_sum_max, nums2_sum  - (nums2[j] - nums2[i-1]) + nums1[j] - nums1[i-1])
        
        return max(nums1_sum_max, nums2_sum_max)
        

