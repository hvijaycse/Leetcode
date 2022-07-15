from typing import List, Optional, Any, Dict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0 

        queue = [root]

        count = 0 
        
        while queue:
            count += 1
            length = len(queue)

            for node in queue[:length]:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            queue = queue[length:]
        
        return count
        
