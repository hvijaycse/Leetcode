from typing import List, Optional, Any, Dict


class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        
        if k == len(cookies):
            return max(cookies)
        
        return self.rec(0, [0]*k, cookies)

    def rec(self, i, kids, cookies):

        if i == len(cookies):
            return max(kids)
        
        ans = float('inf')
        for k in range(len(kids)):
            kids[k] += cookies[i]
            ans = min(ans, self.rec(i + 1, kids, cookies ))
            kids[k] -= cookies[i]
        
        return ans
        

