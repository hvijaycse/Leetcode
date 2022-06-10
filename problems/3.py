from typing import List, Optional, Any, Dict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        lastIndex = {}
        length = 0
        start = -1

        for index in range(len(s)):

            if s[index] in lastIndex:
                start = lastIndex[s[index]]
            
            length = max(length, index - start)

            lastIndex[s[index]] = index
        
        return length
