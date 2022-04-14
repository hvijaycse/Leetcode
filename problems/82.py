from typing import List, Optional, Any, Dict


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: ListNode = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Good question
        '''

        if not head or not head.next:
            return head
        
        new_head = ListNode(val=0, next=head)
        current_node = new_head

        while current_node.next:

            next_node = current_node.next
            

            while next_node.next and next_node.next.val == current_node.next.val:
                next_node = next_node.next
            
            # print(current_node.next.val, next_node.val)
            if next_node.val == current_node.next.val:
                current_node = current_node.next
            else:
                current_node.next = next_node.next
        
        return new_head.next

