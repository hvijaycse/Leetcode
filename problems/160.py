from typing import List, Optional, Any, Dict


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        countA = self.listLen(headA)
        countB = self.listLen(headB)

        if countA > countB:
            for _ in range(countA-countB):
                headA = headA.next
        else:
            for _ in range(countB-countA):
                headB = headB.next

        while headA!=headB:
            headA = headA.next
            headB = headB.next
        
        return headA

    def listLen(self, head):

        count = 0 

        while head:
            head = head.next
            count += 1
        
        return count