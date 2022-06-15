from typing import List, Optional, Any, Dict

class Solution:
    def longestStrChain(self, words: List[str]) -> int:

        maximum_predecessor = 1 

        word_length = {}
        predecessor_count = {}

        for word in words:
            if len(word) in word_length:
                word_length[len(word)].append(word)
            else:
                word_length[len(word)] = [word]
            predecessor_count[word] = 1
        
        lengths = list(word_length.keys())
        lengths.sort()

        for length in lengths[1:]:

            for wordb in word_length.get(length, []):
                for worda in word_length.get(length-1, []):
                    if self.check_predecessor(worda, wordb):
                        predecessor_count[wordb] = max(predecessor_count[wordb], predecessor_count[worda] + 1)
                    maximum_predecessor = max(maximum_predecessor, predecessor_count[wordb])
       
        
        return maximum_predecessor
    
    def check_predecessor(self, worda, wordb):

        if len(worda) +1 != len(wordb):
            return False
        
        ia, ib = 0, 0
        diff_count = 0

        while ia < len(worda) and ib < len(wordb):

            if worda[ia] == wordb[ib]:
                ia += 1
                ib += 1
            else:
                diff_count += 1
                ib += 1
        
        return diff_count <= 1
