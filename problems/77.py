from re import M
from typing import List, Optional, Any, Dict

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        if n == 1:
            return [ i for i in range(1, n+1)]
           