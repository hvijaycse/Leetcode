from typing import List, Optional, Any, Dict

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Total time complexity : O(nlog(n))
        '''
        if head is None or head.next is None:
            return head

        mid = self.getMid(head) # O(n)
        
        midNext = mid.next
        mid.next = None

        head = self.sortList(head) #O(T(n/2))
        midNext = self.sortList(midNext) #O(T(n/2))

        return self.merge(head, midNext) # O(n)

    def getMid(self, head: ListNode):

        if head is None:
            return None

        slow: ListNode = head
        fast: ListNode = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow



    def merge(self, head1: ListNode, head2: ListNode) -> ListNode:
        
        newHead = ListNode(0)
        previous = newHead

        while head1 is not None and head2 is not None:

            if head1.val < head2.val:
                previous.next = head1
                head1 = head1.next
            else:
                previous.next = head2
                head2 = head2.next
            
            previous = previous.next
        
        if head1 is not None:
            previous.next = head1
        else:
            previous.next = head2
        
        return newHead.next
