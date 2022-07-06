from typing import List, Optional, Any, Dict


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        counter = dict()
        
        for num in arr1:    
            counter[num] = counter.get(num, 0) + 1
        
        output = [0 for _ in range(len(arr1))]

        i = 0 

        for num in arr2:

            for _ in range(counter.get(num, 0)):
                output[i] = num
                i += 1
            counter[num] = 0 
        
        arr1.sort()
        for num in arr1:

            if counter[num] > 0:
                output[i] = num
                counter[num] -= 1
                i += 1
        return output
