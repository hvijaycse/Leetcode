from typing import List, Optional, Any, Dict
from timeDec import timeit

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:

        answers = [ 0 for _ in range(len(queries))]
        nums.sort()

        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        
        for index, query in enumerate(queries):

            answers[index] = self.binarySearch(nums, query)  + 1
        
        return answers
            
    
    def binarySearch(self, nums: list[int], target: int) -> int:

        low = 0
        high = len(nums)
        mid = (low + high ) // 2

        while low < high:

            mid = (low + high ) // 2

            if nums[mid] == target:
                return mid
            
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid
        
        if nums[mid] > target:
            mid -= 1
        
        return mid
