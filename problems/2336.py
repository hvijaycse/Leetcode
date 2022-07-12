from typing import List, Optional, Any, Dict

class SmallestInfiniteSet:

    def __init__(self):
        self.numbers = [1,2]
        

    def popSmallest(self) -> int:
        
        smallest = self.numbers.pop(0)
        self.numbers.append(self.numbers[-1]+1)

        return smallest

    def addBack(self, num: int) -> None:

        if num < self.numbers[-1]:

            index = self.binary(num, self.numbers)

            if self.numbers[index] != num:
                self.numbers.insert(index, num)
    
    def binary(self, target, arr):

        low = 0 
        high = len(arr)

        while low < high:
            
            mid = (low + high) // 2

            if arr[mid] == target:
                return mid
            
            elif arr[mid] < target:
                low  = mid + 1
            else:
                high = mid
        
        
        return low
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
