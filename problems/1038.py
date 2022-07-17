from typing import List, Optional, Any, Dict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        
        self.inorder(root,0)

        return root

    def inorder(self, root, last_value) -> int:

        if root is None:
            return last_value
        
        last_value = self.inorder(root.right, last_value)

        root.val += last_value

        last_value = self.inorder(root.left, root.val)

        return last_value

