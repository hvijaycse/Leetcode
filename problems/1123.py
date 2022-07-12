from typing import List, Optional, Any, Dict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        pass
        



    def lcaBST(root: TreeNode, p: TreeNode, q: TreeNode) :

        while root:

            if root == p or root == q:
                return root
            
            elif root.val > p.val and root.val > q.val:
                root = root.left
            
            elif root.val < p.val and root.val < q.val:
                root = root.right
            
            else:
                return root