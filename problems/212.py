import re
from typing import List, Optional, Any, Dict

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        '''
        need to learn trie
        '''
        

        rows = len(board)
        columns = len(board[0])

        Visited = [
            [ False for _ in range(columns) ] for _ in range(rows)
        ]

        starting_index = {}

        for r in range(rows):
            for c in range(columns):
                char = board[r][c]
                if char in starting_index:
                    starting_index[char].append([r,c])
                else:
                    starting_index[char]=[[r,c]]
        word_possible = {
            word: False for word in words
        }
        def backtracking(output: list, r, c, index, word):

            if r < 0 or r >= rows or c < 0 or c >= columns:
                return

            if Visited[r][c]:
                return
            
            if board[r][c] != word[index]:
                return
            
            if index + 1 == len(word):
                if not word_possible[word]:
                    output.append(word)
                word_possible[word] = True
                return
            
            Visited[r][c] = True
            backtracking(output, r+1, c, index+1, word)
            backtracking(output, r-1, c, index+1, word)
            backtracking(output, r, c+1, index+1, word)
            backtracking(output, r, c-1, index+1, word)
            Visited[r][c] = False

        output = []
        for word in words:
            if word[0] not in starting_index:
                continue

            for r,c in starting_index[word[0]]:
                backtracking(output, r,c, 0, word)
                if word_possible[word]:
                    break
        
        return output



