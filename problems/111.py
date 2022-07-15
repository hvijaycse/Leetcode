from typing import List, Optional, Any, Dict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0 

        queue = [root]

        count = 0

        while queue:

            count += 1
            next_queue = []
            for root in queue:

                if root.left is None and root.right is None:
                    return count
                
                if root.left:
                    next_queue.append(root.left)
                if root.right:
                    next_queue.append(root.right)
            
            queue = next_queue
            