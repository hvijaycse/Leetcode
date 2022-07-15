from typing import List, Optional, Any, Dict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:

        inorder = []

        self.inorder(root, inorder)

        return self.build(inorder)
    
    def build(self, inorder):

        if len(inorder) < 1:
            return None
        
        mid = len(inorder) // 2

        current = TreeNode(inorder[mid])

        current.left = self.build(inorder[:mid])
        current.right = self.build(inorder[mid + 1:])

        return current

    def inorder(self, root, inorder):

        if root is None:
            return 
        self.inorder(root.left, inorder)
        
        inorder.append(root.val)

        self.inorder(root.right, inorder)
        

