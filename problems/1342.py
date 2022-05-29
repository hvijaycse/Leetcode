from typing import List, Optional, Any, Dict


class Solution:
    def numberOfSteps(self, num: int) -> int:
        
        count = 0

        while num:

            if (num & 1) % 2:
                count += 2
            else:
                count += 1
            
            num = num >> 1
        return count-1
