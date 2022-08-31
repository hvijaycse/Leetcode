from typing import List, Optional, Any, Dict
from timeDec import timeit


class Solution:
    def largestPalindromic(self, num: str) -> str:
        
        Count = {
            str(i): 0 for i in range(10)
        }

        ans = ""

        for char in num:
            Count[char] += 1
        
        for num in range(9, 0, -1):
            char = str(num)

            ans += char * ( Count[char] // 2)
            Count[char]  = Count[char] % 2
        
        if len(ans) != 0:
            ans += '0' * ( Count['0'] // 2 )
            Count['0']  = Count['0'] % 2


        for num in range(9, -1, -1):
            char = str(num)

            if Count[char] > 0 :
                return ans + char + ans[::-1]

        return ans + ans[::-1]            
