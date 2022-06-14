from typing import List, Optional, Any, Dict

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        rows = len(word1) + 1
        columns = len(word2) + 1
        

        dp = [
            [0 for _ in range(columns)]
            for _ in range(rows)
        ]


        for r in range(1, rows):
            for c in range(1, columns):

                if word1[r-1] == word2[c-1]:
                    dp[r][c] = dp[r-1][c-1] + 1
                else:
                    dp[r][c] = max(dp[r-1][c], dp[r][c-1])
        
        return len(word1) - dp[rows-1][columns-1] + len(word2) - dp[rows-1][columns-1] 
        