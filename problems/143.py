# from typing import List, Optional, Any, Dict


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        middle_node = self.get_middle(head)

        head1 = head
        head2 = self.reverse_list(middle_node.next)
        middle_node.next = None

        new_head = ListNode()
        current = new_head
        even = True

        while head1 is not None and head2 is not None:
            
            if even:
                current.next = head1
                head1 = head1.next
            else:
                current.next = head2
                head2 = head2.next
            
            even = not even
            current = current.next
        
        if head1 is None:
            current.next = head2
        else:
            current.next = head1
        
        
        return new_head.next



    def get_middle(self, head: ListNode):

        if head is None:
            return None
        
        slow: ListNode = head
        fast: ListNode = head.next

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        

        return slow
        

    
    def reverse_list(self, head: ListNode):

        previous = None

        while head is not None:

            next_node = head.next
            head.next = previous
            previous = head
            head = next_node
        
        return previous