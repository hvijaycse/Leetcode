from typing import List, Optional, Any, Dict
from timeDec import timeit
from functools import lru_cache

class Solution:
	# @param A : list of list of integers
	# @return an integer

	def adjacent(self, A):

		N = len(A[0])
		maximum = [0] * N


		for index in range(N):

			current = max(A[0][index], A[1][index])
			max_val = current

			if index - 1 > -1:
				max_val = max(max_val, maximum[index-1])
			if index -2 > -1:
				max_val = max(
					max_val, 
					current + maximum[index-2]
				)
			
			maximum[index] = max_val
		
		return maximum[-1]
			

