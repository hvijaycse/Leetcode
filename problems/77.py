from typing import List, Optional, Any, Dict

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return self.combinator(1, n, k)

    def combinator(self, start: int, end: int, k: int) -> List[List[int]]:
        if k == 1:
            return [[ num] for num in range(start, end + 1)]

        combinations = []

        for number in range(start, end - k + 2):
            more_possible = self.combinator(number + 1, end, k-1)
            for combination in more_possible:
                combinations.append(
                    [number] + combination
                )
            
        return combinations