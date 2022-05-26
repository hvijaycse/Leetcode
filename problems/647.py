from typing import List, Optional, Any, Dict


class Solution:
    def countSubstrings(self, s: str) -> int:
        
        substrings = []
        self.genSubstrings(substrings, s)
        palindromes = []

        for substring in substrings:
            if self.checkPalindrome(substring):
                palindromes.append(substring)
        
        return len(palindromes)

    def checkPalindrome(self, string):
        return string == string[::-1]

    def genSubstrings(self, substrings, string):

        for i in range(len(string)):
            for j in range(i+1, len(string)+1):
                substrings.append(string[i:j])
        