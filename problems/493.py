from typing import List, Optional, Any, Dict

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        pass

    def mergeSort(self, array, low, high):

        reversePair = 0

        if low < high:

            mid = (low + high) // 2

            reversePair += self.mergeSort(array, low, mid)
            reversePair += self.mergeSort(array, mid+1, high)

            reversePair += self.merge(array, low, mid, high)

        return reversePair
    
    def merge(self, array, low, mid, high):

        count = 0 
        
        temp_array = [0 for _ in range(high-low)]

        firstIndex = low
        secondIndex = mid+1
        index = 0 

        while firstIndex < mid + 1 and secondIndex < high:

            if array[firstIndex] < array[secondIndex]:
                temp_array[index] = array[firstIndex]
                firstIndex += 1
            else:
                if array[firstIndex] > 2* array[secondIndex]:
                    count += 1
                temp_array[index] = array[secondIndex]
                secondIndex += 1
        
        if firstIndex < mid + 1:
            while firstIndex < mid + 1:
                temp_array[index] = array[firstIndex]
                firstIndex += 1
                index += 1
        else:
            while secondIndex < high:
                temp_array[index] = array[secondIndex]
                secondIndex += 1
                index += 1
        
        for index in range(high - low):
            


