from typing import List, Optional, Any, Dict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def __init__(self) -> None:
        self.total = 0 
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(root: TreeNode):
            if root:
                dfs(root.right)
                root.val += self.total
                self.total = root.val
                dfs(root.left)

        dfs(root)

        return root
    