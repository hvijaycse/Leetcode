from typing import List, Optional, Any, Dict
import heapq

class Solution:
	# @param A : integer
	# @param B : list of integers
	# @return an integer
    def nchoc(self, A, B):

        mod = 10**9 + 7
        heap = [-chocolate for chocolate in B]

        heapq.heapify(heap)

        eaten = 0 

        for _ in range(A):

            maxChoc = heapq.heappop(heap)
            if maxChoc == 0:
                break
            eaten += -maxChoc % mod

            heapq.heappush(heap, maxChoc // 2)
        
        return eaten % mod