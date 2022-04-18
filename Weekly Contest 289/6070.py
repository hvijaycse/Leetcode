from typing import List, Optional, Any, Dict


class Solution:
    def digitSum(self, s: str, k: int) -> str:
        
        while len(s) > k:
            s = ''.join(
                [
                    str(sum(map(int, [j for j in s[i: i + k]]))) for i in range(0, len(s), k)
                ]
            )
        
        return s

    

# print(Solution().digitSum("11111222223", 3))