from typing import List, Optional, Any, Dict


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        
        Counter = {}

        for item in tasks:
            if item not in Counter:
                Counter[item] = 1
            else:
                Counter[item] += 1
        def dfs(number):
            if number == 0:
                return 0 
            elif number == 1:
                return -1
            else:
                minimum = float('inf')
                for i in range(number//3, -1, -1):
                    remainder = number - i*3
                    if remainder == 1:
                        continue
                    else:
                        minimum = min(minimum, i + remainder//2)
                
                return remainder if remainder != float('inf') else -1
        rounds = 0
        for k , v in Counter.items():
            check = dfs(v)
            if check == -1:
                return -1 
            rounds += check


        return rounds
