from typing import List, Optional, Any, Dict

class WordNode:

    def __init__(self) -> None:
        self.childs = {}
        self.isWord = True


class Trie:
    
    def __init__(self) -> None:
        self.head = WordNode()
    
    def insertWord(self, word):

        current = self.head

        for char in word:
            current.childs[char] = current.childs.get(char, WordNode())
            current = current.childs[char]
        
        current.isWord = True

        return current



class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        
        words.sort(key= lambda x: len(x), reverse=True)

        myTrie = Trie()
        totalLength = 0 
        lastNodes = set()

        for word in words:
            lastNode = myTrie.insertWord(reversed(word))

            if len(lastNode.childs) == 0 or lastNode not in lastNodes:
                totalLength += len(word) + 1
                lastNodes.add(lastNode)
        
        return totalLength