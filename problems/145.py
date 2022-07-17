from typing import List, Optional, Any, Dict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        

        traversal = []
        stack = []

        while root:

            if root.left is None:
                stack.append(root)
                root = root.right
                continue

            leftNode = root.left

            while leftNode.right is not None and leftNode.right != root:
                leftNode = leftNode.right

            
            if leftNode.right is None:
                leftNode.right = root
                stack.append(root)
                root = root.left
            
            else:
                leftNode.right = None
                while stack[-1] != root:
                    temp = stack.pop()
                    traversal.append(temp.val)
                
                root = root.right
        
        while stack:
            temp = stack.pop()
            traversal.append(temp.val)
        
        return traversal
