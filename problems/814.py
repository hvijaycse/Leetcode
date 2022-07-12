from logging.handlers import RotatingFileHandler
from typing import List, Optional, Any, Dict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        total, root = self.dfs(root)

        if total == 0:
            root = None
        
        return root

    def dfs(self, root):
        # This return sum of all
        # node in Sub tree and root of subtree

        if not root:
            return (0, None)
        
        left_sum, left_node = self.dfs(root.left)
        right_sum, right_node = self.dfs(root.right)

        if left_sum == 0:
            root.left = None
        if right_sum == 0 :
            root.right = None
        
        return (left_sum+right_sum + root.val , root)