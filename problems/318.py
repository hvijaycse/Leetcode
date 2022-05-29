from typing import List, Optional, Any, Dict

class Solution:
    def maxProduct(self, words: List[str]) -> int:

        # words = [set(word) for word in words]

        max_length = 0 

        word_len = {}
        
        for word in words:

            mask = 0 
            for char in word:
                mask |= 1 <<(ord(char) - 97)

            word_len[mask] = max(word_len.get(mask,0), len(word))
        

        for w1 in words:
            for w2 in words:
                if not w1 & w2:
                    max_length = max(max_length, word_len[w1] * word_len[w2])
        

        return word_len