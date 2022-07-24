from typing import List, Optional, Any, Dict

class myString:

    def __init__(self, val: int) -> None:
        self.val = str(val)
    
    def __lt__(self, other: 'myString') -> bool:
        return self.val + other.val < other.val + self.val
    
    def __str__(self) -> str:
        return self.val
    
class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        nums = list(map(myString, nums))

        nums.sort(reverse=True)
        
        answer = ''.join(map(str, nums))

        if answer[0] == '0':
            answer = '0'
        
        return answer
    

  
print(Solution().largestNumber(
    [10,2] # 43243243, 43243432
))