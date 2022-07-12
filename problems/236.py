from typing import List, Optional, Any, Dict
from warnings import resetwarnings


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        while root:

            if root == p or root == q:
                return root
            
            left_has_p = self.has_node(root.left, p)
            right_has_q = self.has_node(root.right, q)

            if not(left_has_p ^ right_has_q):
                return root
            
            elif left_has_p:
                root = root.left
            else:
                root = root.right
                

    def has_node(self, root: TreeNode, target: TreeNode):

        if root is None:
            return False

        if root == target:
            return True
        
        return self.has_node(root.left, target) or self.has_node(root.right, target)