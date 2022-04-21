from typing import List, Optional, Any, Dict



class Solution:

    def __init__(self) -> None:
        self.primes = [2, 3, 5, 7, 11 ,13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 107]

    def convert(self, chars: str) -> int:

        answer = 1
        for char in chars:
            answer *= self.primes[ord(char) - 97]
        return answer

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        self.dict = {}

        for string in strs:
            convert_val = self.convert(string)
            if convert_val not in self.dict:
                self.dict[convert_val] = [string]
            else:
                self.dict[convert_val].append(string)
        
        return [list(value) for value in self.dict.values()]
