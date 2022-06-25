from typing import List, Optional, Any, Dict


class Node:

    def __init__(self) -> None:
        self.is_word = False
        self.next_node = {}
    
    def insert_char(self, char):
        self.next_node[char] = self.next_node.get(char, Node())
        return self.next_node[char]
        
class Trie:

    def __init__(self) -> None:
        self.head:Node = Node()
    
    def addWord(self, word):

        tmp = self.head
        for char in word:
            print(tmp.next_node)
            tmp = tmp.insert_char(char)
        
        tmp.is_word = True
    
    
class WordDictionary:

    def __init__(self):
        self.myTrie = Trie()


    def addWord(self, word: str) -> None:
        self.myTrie.addWord(word)
        

    def search(self, word: str) -> bool:

        previous_nodes: List[Node]  = [self.myTrie.head]

        for char in word:
            next_nodes = []

            for node in previous_nodes:
                if not node:
                    continue
                if char == '.':
                    next_nodes += node.next_node.values()
                else:
                    next_nodes.append(node.next_node.get(char, None))

            previous_nodes = next_nodes
        
        for node in previous_nodes:
            if node and node.is_word:
                return True
        
        return False
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
