from typing import List, Optional, Any, Dict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        queue = [cloned]

        while queue:
            node = queue.pop(0)

            if node.val == target.val:
                return node
            
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
            
            
