from typing import List, Optional, Any, Dict


class charNode:

    def __init__(self) -> None:
        self.childs = {}
        self.isword = False
        self.suggestion = []
    
    def insertSuggestion(self, word):

        if len(self.suggestion) < 3:
            self.suggestion.append(word)
        

class Trie:

    def __init__(self) -> None:
        self.head = charNode()
    
    def insertWord(self, word):

        current: charNode = self.head

        for char in word:
            current.childs[char] = current.childs.get(char, charNode())
            current = current.childs[char]
            current.insertSuggestion(word)
    
        
        current.isword = True
    

class Solution:

    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:

        self.myTrie = Trie()
        
        products = sorted(products)

        for product in products:
            self.myTrie.insertWord(product)
        
        answers = []
        current = self.myTrie.head

        for index in range(len(searchWord)):
            current = current.childs.get(searchWord[index], charNode())
            answers.append(current.suggestion)
        return answers
    


