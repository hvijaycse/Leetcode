from turtle import left
from typing import List, Optional, Any, Dict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        traversal = []

        while root:

            if root.left is None:
                traversal.append(root.val)    
                root = root.right
                continue

            leftNode = root.left

            while leftNode.right is not None and leftNode.right != root:
                leftNode = leftNode.right
            
            if leftNode.right is None:
                traversal.append(root.val)    
                leftNode.right = root
                root = root.left
            else:
                leftNode.right = None
                root = root.right
        
        return traversal
