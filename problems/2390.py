from typing import List, Optional, Any, Dict
from timeDec import timeit

class Solution:
    def removeStars(self, s: str) -> str:
        

        answer = ""
        index = 0 

        while index < len(s):

            if s[index] != '*':
                answer += s[index]
                index += 1
                continue

            count = 0
            while index < len(s) and s[index] == '*':
                count += 1
                index += 1
            
            answer = answer[:-count]
        
        return answer