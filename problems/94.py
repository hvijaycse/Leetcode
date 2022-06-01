from typing import List, Optional, Any, Dict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        path = []

        while root:

            if root.left is None:
                path.append(root.val)
                root = root.right

            else:

                left_node: TreeNode = root.left

                while left_node.right is not None and left_node.right != root:
                    left_node = left_node.right
                
                if left_node.right is None:
                    left_node.right = root
                    root = root.left
                else:
                    left_node.right = None
                    path.append(root.val)
                    root = root.right
            
        return path
