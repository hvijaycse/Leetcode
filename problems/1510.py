from typing import List, Optional, Any, Dict

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        
        answer = [False for _ in range(n+1)]

        i = 0 
        while i * i <= n:
            answer[i * i] = True
            i += 1

        for i in range(2, n + 1):

            if answer[i]:
                continue

            j = 1
            any_true = False 

            while j * j < i:
                any_true = any_true or not answer[i - j*j]
                j += 1
            
            answer[i] = any_true
        return answer[n]


# print(Solution().winnerSquareGame(8))