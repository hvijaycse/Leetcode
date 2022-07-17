from typing import List, Optional, Any, Dict

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        
        counter = {}

        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        even = 0
        odd = 0 

        for count in counter.values():

            even += count // 2
            odd += count % 2
        
        return [even, odd]