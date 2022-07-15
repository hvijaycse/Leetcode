from typing import List, Optional, Any, Dict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        self.firstNode = None
        self.secondNode = None

        self.inorder(root, TreeNode(float('-inf')))

        self.firstNode, self.secondNode = self.secondNode, self.firstNode

       



    def inorder(self, root, prev_node):
        

        if root is None:
            return prev_node
        
        last_node = self.inorder(root.left, prev_node)

        if last_node.val > root.val:
            if self.firstNode is None:
                self.firstNode = last_node
                self.secondNode = root
            else:
                self.secondNode = last_node

        return self.inorder(root.right, root)