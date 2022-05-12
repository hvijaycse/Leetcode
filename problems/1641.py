from typing import List, Optional, Any, Dict


class Solution:
    def countVowelStrings(self, n: int) -> int:
        
        counter = {
            1:1,
            2:1,
            3:1,
            4:1,
            5:1
        }

        for _ in range(n-1):
            for i in range(1,5):
                summer = 0
                for j in range(i,6):
                    summer += counter[j]
                counter[i] = summer
        
        return sum(counter.values())