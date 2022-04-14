from typing import List, Optional, Any, Dict


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        '''
        First Solution using backtracking without getting any error in first attempt.
        '''

        rows = len(board)
        columns = len(board[0])


        def backtracking(r, c, reamining_word)-> bool:
            
            if not reamining_word:
                return True

            if reamining_word[0] != board[r][c]:
                return False

            else:
                board[r][c] ='.'

                if backtracking(max(r-1, 0), c, reamining_word[1:]):
                    return True
                elif backtracking(min(r+1, rows-1), c, reamining_word[1:]):
                    return True
                elif backtracking(r, max(0, c-1), reamining_word[1:]):
                    return True
                elif backtracking(r, min(c+1, columns -1), reamining_word[1:]):
                    return True

                board[r][c] = reamining_word[0]

                return False
        

        for r in range(rows):
            for c in range(columns):
                if board[r][c] == word[0] and backtracking(r, c, word):
                    return True
        
        return False