from typing import List, Optional, Any, Dict


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        current_node = head

        while current_node:

            next_node = current_node

            while next_node and next_node.val == current_node.val:
                next_node = next_node.next
            
            current_node.next = next_node

            current_node = current_node.next

        
        return head