from typing import List, Optional, Any, Dict


class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        

        max_diff = 0 

        i = 0 
        j = 0 

        while i < len(nums1) and j < len(nums2):

            if i <= j and nums1[i] <= nums2[j]:
                max_diff = max(max_diff, j-i)
                j += 1
            
            elif i <= j and nums1[i] > nums2[j]:
                i += 1
            
            elif i > j:
                j = i
            
        
        return max_diff