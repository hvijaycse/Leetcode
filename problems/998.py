from typing import List, Optional, Any, Dict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        newNode = TreeNode(val)

        if root is None:
            #  we were given an empty tree
            root = newNode

        elif root.val < newNode.val:
            # value is greated of all time
            newNode.left = root
            root = newNode

        else:
            # value is not greated of all time
            temp = root

            while temp.right is not None and temp.right.val > val:
                temp = temp.right
            
            if temp.right is not None:
                newNode.left = temp.right
            
            temp.right = newNode
        
        return root
