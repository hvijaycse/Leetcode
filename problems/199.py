from typing import List, Optional, Any, Dict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        right_view = [ None for _ in range(100)]

        index = 0 

        queue = [(root, 0 )]

        while queue:

            node, index = queue.pop(0)

            if node is None:
                continue

            if right_view[index] is None:
                right_view[index] = node.val
            
            queue.append((node.right, index + 1))
            queue.append((node.left, index + 1))
        
        return right_view[:index]

