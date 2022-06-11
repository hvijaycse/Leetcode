from typing import List, Optional, Any, Dict



class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:

        totalSum = sum(nums)
        remaining = totalSum - x

        if remaining < 0:
            return -1 
        if remaining == 0:
            return len(nums)
        
        length = -1
        start = -1
        current = 0

        for end in range(len(nums)):

            current += nums[end]

            while current >= remaining:

                if current == remaining:
                    length = max(length, end-start)
                current -= nums[start + 1]
                start += 1
        
        return -1 if length == -1 else len(nums) - length

        

    def bruteForce(self, nums, left, right,  target):
        '''
        Brute Force method,
        this try all possible solutions
        '''
        if target == 0 :
            return 0
        
        if left > right:
            return -1
        
        if nums[left] > target and nums[right] > target:
            return -1
        
        if nums[left] == target or nums[right] == target:
            return 1
        
        leftMove = -1
        rightMove = -1

        if nums[left] < target:
            leftMove = self.bruteForce(nums, left +1, right, target-nums[left])
        if nums[right] < target:
            rightMove = self.bruteForce(nums, left , right-1, target-nums[right])
        
        if leftMove == -1 and rightMove == -1:
            return -1
        
        if leftMove == - 1:
            return rightMove +  1
        
        if rightMove == -1:
            return leftMove + 1

        return min(leftMove, rightMove) + 1