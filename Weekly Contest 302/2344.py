from typing import List, Optional, Any, Dict

class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        
        gcd = 0 

        for num in numsDivide:
            gcd = self.gcd(gcd, num)
        
        smallerCount = 0 
        isPresent = False
        smallest = gcd

        for num in nums:

            if gcd % num == 0:
                smallest = min(smallest, num)
        
        for num in nums:

            if smallest == num:
                isPresent = True
            elif num < smallest:
                smallerCount += 1

        if isPresent:
            return smallerCount
        return -1

    def gcd(self, a, b):
        while a:
            a,b = b%a, a 
        return b
