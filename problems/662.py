from typing import List, Optional, Any, Dict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class node:

    def __init__(self, root: TreeNode, location: int) -> None:
        self.root = root
        self.location = location
        
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        if root is None:
            return 0

        max_width = 0

        queue: List[node] = [
            node(root, 1)
        ]

        while queue:
            length = len(queue)
            first, last = queue[0], queue[-1]

            max_width = max(max_width, last.location - first.location + 1)

            for item in queue[:length]:

                if item.root.left:

                    queue.append(
                        node(item.root.left, item.location * 2-1)
                    )
                if item.root.right:

                    queue.append(
                        node(item.root.right, item.location * 2)
                    )
            queue = queue[length: ]
            
            
        
        return max_width
