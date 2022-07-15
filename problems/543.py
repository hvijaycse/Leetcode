from typing import List, Optional, Any, Dict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        _, diameter = self.postOrder(root)

        return diameter

    def postOrder(self, root):
        # This return the height of the 
        # tree and diameter of the tree
        if not root:
            return (0, 0)
        
        lHeight, lDiameter = self.postOrder(root.left)
        rHeight, rDiameter = self.postOrder(root.right)

        height = max(lHeight, rHeight) + 1
        diameter = max(lDiameter, rDiameter, lHeight + rHeight )

        return (height, diameter)
        


