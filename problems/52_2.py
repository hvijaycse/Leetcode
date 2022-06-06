from typing import List, Optional, Any, Dict

class Solution:
    def totalNQueens(self, n: int) -> int:
        
        self.rows = set()
        self.columns = set()
        self.daigonal = set()
        self.offDaigonal = set()
        self.n = n
        self.count = 0
        self.backtracking(0)

        return self.count

    def backtracking(self, r: int):
        if r == self.n:
            self.count += 1
            return
        else:
            for c in range(self.n):

                if r in self.rows:
                    continue
                if c in self.columns:
                    continue

                if r-c in self.daigonal:
                    continue

                if r + c in self.offDaigonal:
                    continue

                self.rows.add(r)
                self.columns.add(c)
                self.offDaigonal.add(r+c)
                self.daigonal.add(r-c)
                
                self.backtracking(r+1)

                self.rows.remove(r)
                self.columns.remove(c)
                self.offDaigonal.remove(r+c)
                self.daigonal.remove(r-c)


