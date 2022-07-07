from typing import List, Optional, Any, Dict

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        middle_node = self.get_middle(head)


        head2 = self.reverse_list(middle_node.next)

        while head and head2:
            if head.val != head2.val:
                return False
            head = head.next
            head2 = head2.next

        return True 


    def reverse_list(self, head):

        prev = None

        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        
        return prev



    def get_middle(self, head) :

        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow
