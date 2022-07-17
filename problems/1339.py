from typing import List, Optional, Any, Dict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        mod = 1000000007
        self.maxProduct = float('-inf')

        total = self.getSum(root)
        self.calMax(root, total)

        return self.maxProduct % mod
    
    def calMax(self, root, total):

        if root is None:
            return 
        
        self.calMax(root.right, total)

        if root.left:
            self.calMax(root.left, total)
            self.maxProduct = max(self.maxProduct, (total - root.left.val) * root.left.val)

        if root.right:
            self.calMax(root.right, total)
            self.maxProduct = max(self.maxProduct, (total - root.right.val) * root.right.val)
        
        return 
        

    def getSum(self, root: TreeNode):

        if root is None:
            return 0
        
        root.val += self.getSum(root.left) + self.getSum(root.right)

        return root.val
