from typing import List, Optional, Any, Dict


class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        answer = 1
        isInverse = False
        if n < 0:
            isInverse = True
            n = abs(n)


        while n:

            if n % 2:
                answer *= x
                n-=1
            else:

                n = n // 2
                x = x * x
        
        return 1/answer if isInverse else answer
