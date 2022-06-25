# from typing import List, Optional, Any, Dict



class WordFilter:

    def __init__(self, words: List[str]):
        self.myTrie = {}

        for index, word in enumerate(words):
            for i in range(len(word)+1):
                node = self.myTrie
                node['index'] = index
                word_to_insert = word[i:] + '@' + word
                for char in word_to_insert:
                    node[char] = node.get(char, {})
                    node = node[char]
                    node['index'] = index
            
        
    def f(self, prefix: str, suffix: str) -> int:
        
        word = suffix + '@' + prefix
        current = self.myTrie

        for char in word:
            if char not in current:
                return -1
            current = current[char]
        
        return current['index']

# Your WordFilter object will be instantiated and called as such:
# words = ['apple']
# obj = WordFilter(words)
# param_1 = obj.f('a','l')
