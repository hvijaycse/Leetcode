from typing import List, Optional, Any, Dict



from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

import heapq

def connectRopes( arr, n) :

	# Your code goes here

	heapq.heapify(arr)
	cost = 0 
	while len(arr) > 1:

		first = heapq.heappop(arr)
		second = heapq.heappop(arr)

		cost += first + second

		heapq.heappush(arr, first+second)
	
	return cost































#taking inpit using fast I/O
def takeInput() :
	n = int(input())

	if n == 0 :
		return list(), 0

	arr = list(map(int, stdin.readline().strip().split(" ")))

	return arr, n


#main
arr, n = takeInput()
print(connectRopes( arr, n))

