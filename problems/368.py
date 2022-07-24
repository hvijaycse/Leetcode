from typing import List, Optional, Any, Dict



class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        
        nums.sort()

        answer = []
        index = 0

        while nums[index] == 0:
            index += 1
        
        answer = nums[:index]

        remaining = []
        nums = nums[index:]

        used = [False for _ in range(len(nums))]

        while any(used):

            for index in range(len(used)):
                if not used[index]:
                    break

            previous = nums[index]
            used[index] = True

            current = [previous]

            for index in range(index + 1, len(nums)):

                if not used[index] and nums[index] % previous == 0 :
                    current.append(nums[index])
                    used[index] = True
            
            if len(current) > remaining:
                remaining = current
        
        return answer + remaining
    

