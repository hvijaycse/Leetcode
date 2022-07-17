from typing import List, Optional, Any, Dict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        return self.check(root)


    def check(self, root, leftLength=None, rightLength=None):
        if root is None:
            return True

        if leftLength is None:
            leftLength = self.leftLength(root)
        if rightLength is None:
            rightLength = self.rightLength(root)
        
        if  leftLength - rightLength  < 0 or leftLength - rightLength > 2:
            return False
        
        return self.check(root.left, leftLength-1, None) and self.check(root.right, None, rightLength-1)


    def leftLength(self, root):
        length = 0 
        while root is not None:
            root = root.left
            length += 1
        return length

    def rightLength(self, root):
        length = 0 
        while root is not None:
            root = root.right
            length += 1
        return length
