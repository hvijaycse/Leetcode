from typing import List, Optional, Any, Dict



# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        

        first_head = ListNode()
        last_head = ListNode()

        first_curr = first_head
        last_curr = last_head

        while head:
            if head.val < x:
                first_curr.next = ListNode(head.val)
                first_curr = first_curr.next
            else:
                last_curr.next = ListNode(head.val)
                last_curr = last_curr.next
            
            head = head.next
        
        first_curr.next = last_head.next

        return first_head.next