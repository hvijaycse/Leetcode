from typing import List, Optional, Any, Dict

class Solution:
    def coinChange(self, coins: List[int], amounts: int) -> int:
        

        dp = [float('inf') for _ in range(amounts + 1)]
        dp[0] = 0

        for amount in range(1,amounts+1):

            for coin in coins:

                remaining = amount - coin

                if remaining > -1:
                    dp[amount] = min(dp[amount],dp[remaining] + 1 )
        
        return dp[amounts] if dp[amounts] != float('inf') else -1