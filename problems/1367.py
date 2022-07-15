from typing import List, Optional, Any, Dict


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:

        if head is None:
            return True
        
        if root is None:
            return False
        
        if head.val == root.val:
            if self.checkDFS(head, root):
                return True
        
        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)        

       
    

    def checkDFS(self, head: ListNode, root: TreeNode):

        if head is None:
            return True
        
        if root is None:
            return False
        
        if head.val != root.val:
            return False
        
        return self.checkDFS(head.next, root.left) or self.checkDFS(head.next, root.right)
            