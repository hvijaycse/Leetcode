from typing import List, Optional, Any, Dict

class Solution:
    def countBits(self, n: int) -> List[int]:
        
        if n < 1:
            return [0]
        
        ans = [0 for _ in range(n+1)]
        
        starting = 1 
        next_number = 1 
        last_index = 0 
        current_index = 1

        while current_index <= n:

            if current_index == next_number:
                next_number = next_number << 1
                last_index = 0
            
            ans[current_index] = 1 + ans[last_index]

            last_index += 1
            current_index += 1
        
        return ans