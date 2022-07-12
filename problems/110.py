from typing import List, Optional, Any, Dict

from urllib3 import Retry


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        is_balanced, height = self.check(root)

        return is_balanced

    def check(self, root):
        
        # this will return wheter a tree is balanced or not 
        # plus the height of the tree

        # base case 
        if root is None:
            return (True, 0)
        
        is_balanced = False
        left_balanced, left_height = self.check(root.left)
        right_balanced, right_height = self.check(root.right)

        if left_balanced and right_balanced and abs(left_height - right_height) <= 1 :
            is_balanced = True
        
        return (is_balanced, max(left_height, right_height) + 1)

