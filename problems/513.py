from typing import List, Optional, Any, Dict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:


        left_val, left_level = self.dfs(root, level=0)

        return left_val
    
    def dfs(self, node, level):

        if not node:
            return None, level
        
        if node.left is None and node.right is None:
            return node.val, level
        
        left_val, left_level = self.dfs(node.left, level + 1)
        right_val, right_level = self.dfs(node.right, level + 1)

        if left_val is None:
            return right_val, right_level
            
        elif right_val is None:
            return left_val, left_level
        
        if right_level > left_level:
            return right_val, right_level
        else:
            return left_val, left_level
        