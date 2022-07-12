from typing import List, Optional, Any, Dict


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        deque = []
        answer = []

        for i in range(k):

            while len(deque) > 0 and deque[-1] < nums[i]:
                deque.pop()
            
            deque.append(nums[i])
        
        answer.append(deque[0])

        for i in range(k, len(nums)):

            if deque[0] == nums[i-k]:
                deque.pop(0)
            
            while deque and deque[-1] < nums[i]:
                deque.pop()
            
            deque.append(nums[i])

            answer.append(deque[0])
        
        return answer
        

