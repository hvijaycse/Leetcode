from typing import List, Optional, Any, Dict


class Solution:
    def countAsterisks(self, s: str) -> int:
        
        count = 0 
        isCount = True

        for char in s:
            if char == '|':
                isCount = not isCount
            
            elif char == '*' and isCount:
                count += 1
        
        return count