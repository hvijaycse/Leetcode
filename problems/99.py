from tkinter.tix import Tree
from typing import List, Optional, Any, Dict

from pkg_resources import WorkingSet


# Definition for a binary tree node.
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
        wrongs: List[TreeNode] = []
        def dfs(node: TreeNode, minimum: int, maximum: int):
            if not node:
                return
            else:
                if node.val < minimum or node.val > maximum:
                    wrongs.append(node)

                dfs(node.left, minimum, node.val)
                dfs(node.right, node.val, maximum)

        dfs(root, float('-inf'), float('inf'))
        
        if len(wrongs) == 1:
            wrongs.append(root)
        wrongs[0].val, wrongs[1].val = wrongs[1].val, wrongs[0].val

        return root 