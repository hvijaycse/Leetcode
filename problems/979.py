from typing import List, Optional, Any, Dict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.moves = 0 
        
        self.postOrder(root)

        return self.moves


    def postOrder(self, root):
        
        if root is None:
            return 0

        leftExcess = self.postOrder(root.left)
        rightExcess = self.postOrder(root.right)

        current_node = leftExcess + rightExcess + root.val

        self.moves += abs(current_node - 1)

        return current_node - 1
