from typing import List, Optional, Any, Dict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, right=None, left=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        
        tilt, sum = self.check(root)
        
        return tilt

    def check(self, root):
        
        # return tilt, sum of a root

        if root is None:
            return (0, 0)
        
        left_tilt, left_sum = self.check(root.left)
        right_tilt, right_sum = self.check(root.right)

        tilt = left_tilt + right_tilt + abs(left_sum - right_sum)
        
        return (tilt, left_sum + right_sum + root.val )