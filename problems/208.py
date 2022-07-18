from typing import List, Optional, Any, Dict


class TrieNode:

    def __init__(self) -> None:
        self.isEnd = False
        self.edges = {}


class Trie:

    def __init__(self):
        self.root = TrieNode()        

    def insert(self, word: str) -> None:
        current = self.root

        for char in word:
            if char not in current.edges:
                current.edges[char] = TrieNode()
            current = current.edges[char]
        
        current.isEnd = True        
        

    def search(self, word: str) -> bool:

        current = self.root

        for char in word:

            if char not in current.edges:
                return False
            current = current.edges[char]   

        return current.isEnd     

    def startsWith(self, prefix: str) -> bool:

        current = self.root

        for char in prefix:

            if char not in current.edges:
                return False
            
            current = current.edges[char]
        
        return True
        

