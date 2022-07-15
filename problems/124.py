from typing import List, Optional, Any, Dict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        _, path = self.dfs(root)

        return path

    def dfs(self, root):
        # this return the left_sum, right_max, 

        if root is None:
            return (0, float('-inf'))
        
        left_sum, left_path = self.dfs(root.left)
        right_sum, right_path = self.dfs(root.right)

        this_sum = max(left_sum, right_sum) + root.val
        max_path = max(
            left_path, 
            right_path, 
            root.val + left_sum + right_sum,
            root.val + left_sum, 
            root.val + right_sum
            )
            
        return (this_sum, max_path)