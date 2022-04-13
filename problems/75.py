from typing import List, Optional, Any, Dict


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # Well this problem can be solved by modified counting sort for sorting in O(n) time,
        # but this has an really beutiful approch. 
        # Divide the array into three sections via three pointers.

        red, white, blue = 0, 0, len(nums) - 1 

        while white <= blue:

            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
            elif nums[white] == 1:
                white += 1
            else:
                nums[blue], nums[white] = nums[white], nums[blue]
                blue -= 1
