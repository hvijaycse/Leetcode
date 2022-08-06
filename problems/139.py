from typing import List, Optional, Any, Dict
from timeDec import timeit

from functools import lru_cache


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.string = s
        self.wordDict = set(wordDict)
        return self.foo(0)
    
    @lru_cache(None)
    def foo(self, index:int) -> bool:
        
        if index == len(self.string):
            return True
        
        for end_index in range(index+1, len(self.string)+1):
            if self.string[index: end_index] in self.wordDict and self.foo(end_index):
                return True
            
        
        return False