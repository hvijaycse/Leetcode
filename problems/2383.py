from typing import List, Optional, Any, Dict
from timeDec import timeit


class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        

        minHours = 0
        N = len(energy)

        minHours += max(0, sum(energy) + 1  - initialEnergy)

        for index in range(N):
            minHours += max(0, experience[index] - initialExperience + 1)
            initialExperience += experience[index] + max(0, experience[index] - initialExperience + 1)
        

        return minHours