from typing import List, Optional, Any, Dict



# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        

        queue = [(root, 0)]
        this_sum = 0
        current_level = 0 

        while queue:
            node, level = queue.pop(0)

            if current_level != level:
                current_level = level
                this_sum = 0
            this_sum += node.val

            if node.left:
                queue.append((node.left, level + 1))
                
            if node.right:
                queue.append((node.right, level + 1))
            
            
        return this_sum