from typing import List, Optional, Any, Dict

class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        
        if num == 0:
            return 0
        
        ans = -1

        for i in range(1, 11):

            if (k*i) % 10 == num % 10:
                break

        if num >= k*ans:
            return ans
        
        return -1
