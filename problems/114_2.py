from turtle import left
from typing import List, Optional, Any, Dict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        while root is not None:

            if root.left is not None:
                leftNode = root.left
                while leftNode.right != None:
                    leftNode = leftNode.right
                
                leftNode.right = root.right
                root.right = root.left
                root.left = None
                
            root = root.right
