from typing import List, Optional, Any, Dict

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        

        if head is None:
            return None

        
        newHead = ListNode(
            val = float('-inf'),
            next = head
        )


        previous: ListNode = head
        current: ListNode = head.next

        while current is not None:

            if current.val > previous.val:

                current = current.next
                previous = previous.next
                continue

            nextNode = current.next

            tempHead = newHead
            tempPrev = None

            while tempHead is not None and tempHead.val < current.val:
                tempPrev = tempHead
                tempHead = tempHead.next
            
            tempPrev.next = current
            current.next = tempHead

            previous.next = nextNode
            current = nextNode
        
        return newHead.next