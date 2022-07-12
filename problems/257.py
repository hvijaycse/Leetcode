from typing import List, Optional, Any, Dict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []

        self.rec(root, [], paths)

        return paths

    def rec(self, root, current, paths):

        current.append(str(root.val))
        
        if root.left is None and root.right is None:
            paths.append('->'.join(current))
        else:
            if root.left is not None: self.rec(root.left, current, paths)
            if root.right is not None: self.rec(root.right, current, paths)

        current.pop()

        return
