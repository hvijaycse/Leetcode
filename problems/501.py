import re
from typing import List, Optional, Any, Dict


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        self.mode = []

        current = -1
        frequency = 0
        maxfrequency = 0

        self.inorder(root, current, frequency, maxfrequency)

        return self.mode

    def inorder(self, root, current, frequency, maxfrequency):

        if root is None:
            return
        
        if root.val != current:
            frequency = 1
        else:
            frequency += 1

        if frequency == maxfrequency:
            self.mode.append(root.val)
        elif frequency > maxfrequency:
            self.mode = [root.val]
            maxfrequency = frequency
        
        self.inorder(root.left, root.val, frequency, maxfrequency)
        self.inorder(root.right, root.val, frequency, maxfrequency)