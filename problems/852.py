from re import L
from typing import List, Optional, Any, Dict

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:

        low = 1
        high = len(arr)-1

        while low <= high:
            mid = (low + high) // 2

            if arr[mid-1] < arr[mid] > arr[mid+1]:
                return mid
            
            elif arr[mid-1] < arr[mid]:
                low = mid + 1
            else:
                high = mid
        
        return (low + high)//2