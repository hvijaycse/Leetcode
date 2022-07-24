from typing import List, Optional, Any, Dict



class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        citations.sort()

        low =  0
        high = len(citations)
        ans = 0

        while low < high:

            mid = low + (high - low) // 2
            value = citations[mid]


            if value >= len(citations) - mid:
                ans = max(ans, mid)
                high = mid
            else:
                low = mid + 1
        
        return ans


