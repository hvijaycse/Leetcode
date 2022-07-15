from typing import List, Optional, Any, Dict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        
        return self.preOrder(root, root.val)

    def preOrder(self, root, val) -> bool:
        if not root:
            return True
        if root.val != val:
            return False
        
        return self.preOrder(root.left, val) and self.preOrder(root.right, val)