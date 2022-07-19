import re
from typing import List, Optional, Any, Dict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        if root is None:
            return 0
        
        queue = [root]
        total = 0

        while queue:

            root = queue.pop(0)

            if root is None:
                continue

            if root.val < low:
                queue.append(root.right)
            elif root.val > high:
                queue.append(root.left)
            else:
                total += root.val
                queue.append(root.left)
                queue.append(root.right)
        
        return total
                