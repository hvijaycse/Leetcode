from typing import List, Optional, Any, Dict
from timeDec import timeit



class Solution:

    def numSquares(self, n: int) -> int:

        sqrt = int(n ** 0.5) + 1

        sqaures = [ i * i for i in range(1, sqrt)]

        dp = [float('inf') for _ in range(n + 1)]
        dp[0], dp[1] = 0, 1

        for num in range(n + 1):

            for sq in sqaures:
                if sq > num:
                    break
            
                dp[num] = min(dp[num], 1 + dp[num-sq]) 
        
        return dp[-1]


print(Solution().numSquares(int(1e3)))