from typing import List, Optional, Any, Dict


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        slow = nums[0]
        fast = nums[nums[0]]

        while fast != slow:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        fast = 0

        while fast != slow:
            fast = nums[fast]
            slow = nums[slow]
        
        return fast