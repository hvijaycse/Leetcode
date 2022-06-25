from typing import List, Optional, Any, Dict


class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_length = 0
        left = 0
        right = 0

        for index in range(len(s)):

            r = index + 1

            while r < len(s) and s[r] == s[index]:
                r += 1
            
            l = index - 1

            while l >=0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            
            if r - l + 1 > max_length:
                max_length = r - l + 1
                left = l
                right = r
        
        return s[left + 1: right]