from typing import List, Optional, Any, Dict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        new_node = TreeNode(val)

        if root is None:
            return new_node
        
        temp = root

        while True:

            if val < temp.val:
                if temp.left is None:
                    temp.left = new_node
                    break
                temp = temp.left
            else:

                if temp.right is None:
                    temp.right = new_node
                    break
                temp = temp.right
        
        return root