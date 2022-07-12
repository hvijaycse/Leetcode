from typing import List, Optional, Any, Dict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        min_value = float('-inf')
        current = root

        while current:
            
            if current.left is None:
                if current.val < min_value:
                    return False
                
                min_value = current.val
                current = current.right
                continue
                

            left_node = current.left

            while left_node.right is not None and left_node.right != current:
                left_node = left_node.right
            
            if left_node.right is None:
                left_node.right = current
                current = current.left
            else:
                if current.val < min_value:
                    return False
                min_value = current.val
                left_node.right = None
                current = current.right
            
        return True





