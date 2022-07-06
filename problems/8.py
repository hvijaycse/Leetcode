from typing import List, Optional, Any, Dict


class Solution:
    def myAtoi(self, s: str) -> int:
        
        number = 0 
        is_negative = False
        index = 0 
        limit = 2 ** 31

        while index < len(s) and s[index] == ' ':
            index += 1
        
        if index == len(s):
            return 0
        
        if s[index] == '-':
            is_negative = True
            index += 1
        elif s[index] == '+':
            index += 1
        
        while index < len(s) and  47 < ord(s[index]) < 58:
            number = number * 10
            number += ord(s[index]) - 48
            index += 1
        
        
        if is_negative:
            number *= -1
        
        number = min(max(number, -limit), limit)
        
        return number