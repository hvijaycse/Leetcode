from typing import List, Optional, Any, Dict


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next:ListNode = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if left == right:
            return head
        
        new_head = ListNode(0, head)

        temp=new_head
        prev = None
        index = 0 
        left_prev = None
        right_next = None

        while index <= right + 1:
            if index == left-1:
                left_prev = new_head
            elif index == right+1:
                right_next = new_head
            elif left <= index <= right:
                pass
            else:
                index += 1
                prev = new_head
                new_head.next = new_head