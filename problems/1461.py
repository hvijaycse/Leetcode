from typing import List, Optional, Any, Dict

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:

        substrings = set()

        for i in range(0, len(s)-k+1):
            substrings.add(s[i:i+k])
        
        return len(substrings) == 2**k
