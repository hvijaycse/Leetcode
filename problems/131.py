from typing import List, Optional, Any, Dict
from functools import lru_cache
from timeDec import timeit

class Solution:


    @lru_cache(None)
    def partition(self, s: str) -> List[List[str]]:

        ans = []

        for i in range(1, len(s)):

            currentString = s[:i]
            remainingString = s[i:]

            if self.checkPalin(currentString):
                remainPartitions = self.partition(remainingString)
                for remain in remainPartitions:
                    ans.append([currentString] + remain)
                
        if self.checkPalin(s):
            ans.append([s])

        return ans

    
    def checkPalin(self, string: str) -> bool:
        return string == string[::-1]

        
Solution().partition("aaaaaaaa")
print('__________')
# Solution().partition2("aaaaaaaa")