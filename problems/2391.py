from typing import List, Optional, Any, Dict
from timeDec import timeit

class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        
        Indexes = {
            'M': 0 ,
            'P': 0 ,
            'G': 0 
        }

        totalTime = 0 


        for index, g in enumerate(garbage):
            totalTime += len(g)
            for ty in g:
                Indexes[ty] = index        

        for index in Indexes.values():
            totalTime += sum(travel[:index])
        

        return totalTime
        