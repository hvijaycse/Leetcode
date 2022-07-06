from typing import List, Optional, Any, Dict

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        answer = float('-inf')        
        index = 0 

        while index < len(nums):

            first_negative = 1
            current = 1

            while index < len(nums):

                current *= nums[index]
                index +=1 

                answer = max(answer, current)

                if current < 0 and first_negative > 0:
                    first_negative = current
                elif current < 0:
                    answer = max(answer, current // first_negative)
                elif current == 0:
                    break
                
        
        return answer