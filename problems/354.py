from typing import List, Optional, Any, Dict

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        
        rows = max(envelopes, key= lambda x: x[0])[0]
        columns = max(envelopes, key= lambda x: x[1])[1]
        # print('max', rows, columns)
        Matrix = [
            [ 0 for _ in range(columns + 1)] for _ in range(rows + 1)
        ]

        for envelop in envelopes:
            Matrix[envelop[0]][envelop[1]] = 1

        max_answer = 0
        for r in range(1, rows + 1):
            for c in range(1, columns + 1):
                if Matrix[r][c] == 1:
                    Matrix[r][c] = Matrix[r-1][c-1] + 1
                    max_answer = max(max_answer, Matrix[r][c])
                else:
                    Matrix[r][c] = max(Matrix[r-1][c], Matrix[r][c-1])
        
        return max_answer