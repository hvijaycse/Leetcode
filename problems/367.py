# from typing import List, Optional, Any, Dict

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        if num == 1:
            return True
        

        low = 1
        high = num

        while low < high:

            mid = (low + high) // 2
            if mid * mid == num:
                return True
            elif mid * mid < num:
                low = mid + 1
            else:
                high = mid
        

        return False
