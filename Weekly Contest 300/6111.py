from typing import List, Optional, Any, Dict

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        

        matrix = [ [-1 for _ in range(n) ] for _ in range(m)]

        r, c = 0, -1

        while head:

            for _ in range(n):
                c += 1 

                if head:
                    matrix[r][c] = head.val
                    head = head.next
                else:
                    break
            
            for _ in range(m - 1):
                r += 1

                if head:
                    matrix[r][c] = head.val
                    head = head.next
                else:
                    break
            
            for _ in range(n -1):
                c -= 1
                if head:
                    matrix[r][c] = head.val
                    head = head.next
                else:
                    break
            
            for _ in range(m -2):
                r -= 1
                if head:
                    matrix[r][c] = head.val
                    head = head.next
                else:
                    break
            
            n -= 2
            m -= 2
        
        return matrix