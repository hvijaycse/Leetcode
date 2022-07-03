from typing import List, Optional, Any, Dict 

class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        
        new_people = [0 for _ in range(n)]
        new_people[0] = 1
        mod = 1000000007
        total = 0

        for index in range(n):

            for k in range(index + delay , min(index + forget, n)):
                new_people[k] += new_people[index]
            
            if index + forget > n:
                total += new_people[index] % mod
                    
        return total % mod