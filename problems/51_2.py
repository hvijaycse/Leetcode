from typing import List, Optional, Any, Dict


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        rows = set()
        columns = set()
        daigonal = set()
        otherDaigonal= set()

        board = [
            ['.' for _ in range(n)]
            for _ in range(n)
        ]

        answers = []

        def bactracking(r):
            if r == n:
                answers.append(
                    [''.join(row) for row in board]
                )
            
            for c in range(n):
                if r in rows:
                    continue
                if c in columns:
                    continue
                if r+c in otherDaigonal:
                    continue
                if r - c  in daigonal:
                    continue

                rows.add(r)
                columns.add(c)
                otherDaigonal.add(r+c)
                daigonal.add(r-c)

                board[r][c] = 'Q'

                bactracking(r+1)

                board[r][c] = '.'
                rows.remove(r)
                columns.remove(c)
                otherDaigonal.remove(r+c)
                daigonal.remove(r-c)
        
        bactracking(0)

        return answers