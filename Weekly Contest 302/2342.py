from typing import List, Optional, Any, Dict

class Node:

    def __init__(self, max_value) -> None:
        self.max1 = max_value
        self.max2 = 0
    
    def insert(self, num):
        if num > self.max1:
            self.max2 = self.max1
            self.max1 = num
        elif num > self.max2:
            self.max2 = num
        
    

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        maxValue = -1
        mapping = {}

        for num in nums:
            summer = self.getSum(num)
            if summer not in mapping:
                mapping[summer] = Node(num)
            else:
                mapping[summer].insert(num)
        
        for value in mapping.values():

            if value.max2 == 0:
                continue

            maxValue = max(maxValue, value.max1 + value.max2)
        
        return maxValue



    def getSum(self, number):

        total = 0
        while number:
            total += number % 10
            number = number // 10
        
        return total
