from typing import List, Optional, Any, Dict

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        
        arr2.sort()
        count = 0 

        for num in arr1:
            is_valid = True
            index = self.findIndex(arr2, num)

            if abs(arr2[index] - num) <= d:
                is_valid = False
            if index -1 > -1 and abs(arr2[index-1] -num) <= d:
                is_valid = False
            if index + 1 < len(arr2) and abs(arr2[index + 1] -num) <= d:
                is_valid = False
            
            if is_valid:
                count += 1
        
        return count
            
    
    def findIndex(self, array: List[int], target: int) -> int :

        low = 0
        high = len(array)

        while low < high:
            mid = (low + high) // 2

            if array[mid] == target:
                return mid
            elif target < array[mid]:
                high = mid
            else:
                low = mid + 1
        
        return (low + high) // 2
