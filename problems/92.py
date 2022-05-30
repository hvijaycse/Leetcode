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
        index = 1  
        LOL = None

        while index < left:
            index += 1
            temp = temp.next
        
        LOL = temp
        LeftNode = temp.next

        temp = temp.next
        prev=None
        
        while index <= right:
            index += 1
            next_node = temp.next
            temp.next = prev
            prev = temp
            temp = next_node
        
        LeftNode.next = temp
        LOL.next = prev


        return new_head.next