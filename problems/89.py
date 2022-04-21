from typing import List, Optional, Any, Dict


class Solution:
    def grayCode(self, n: int) -> List[int]:
        
        initial = [0]

        for i in range(n):
            initial += [item | 1 << i for item in reversed(initial) ]
        
        return initial