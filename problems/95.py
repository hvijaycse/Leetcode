from typing import List, Optional, Any, Dict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        root = TreeNode(val=n)
        if n == 1:
            return [root]
        
        smallerTrees = self.generateTrees(n-1)
        generatedTrees = []

       
        

        
        