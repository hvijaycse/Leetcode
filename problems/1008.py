from typing import List, Optional, Any, Dict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        if len(preorder) == 0 :
            return None
        
        root = TreeNode(preorder[0])

        for val in preorder[1:]:
            self.insertBST(root, val)

        return root
    

    def insertBST(self, root, val):

        if root is None:
            return TreeNode(val)

        if val > root.val:
            root.right = self.insertBST(root.right, val)
        else:
            root.left = self.insertBST(root.left, val)
        
        return root