from typing import List, Optional, Any, Dict

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        
        new_head = ListNode(-1, head)
        current = new_head

        for _ in range(left-1):
            current = current.next
        
        right, right_left = self.reverse_k(current.next, right-left+1)
        current.next.next = right_left 
        current.next = right

        return new_head.next
        

    
    def reverse_k(self, node, k ):
        
        previous = None
        next_node = node.next

        while k and node:
            k -=1
            next_node = node.next
            node.next = previous
            previous = node
            node = next_node
        
        return previous, next_node
