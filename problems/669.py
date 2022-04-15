from tkinter.tix import Tree
from typing import List, Optional, Any, Dict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        

        new_root = TreeNode(0, None, root)

        def dfs(parent: TreeNode, child: TreeNode, is_left:bool) :
            
            if not child:
                return
            else:

                if child.val < low:
                    if is_left:
                        parent.left = child.right
                        dfs(parent, parent.left, True)
                    else:
                        parent.right = child.right
                        dfs(parent, parent.right, False)
                
                elif child.val > high:
                    if is_left:
                        parent.left = child.left
                        dfs(parent, parent.left, True)
                    else:
                        parent.right = child.left
                        dfs(parent, parent.right, False)
                else:
                    dfs(child, child.left, True)
                    dfs(child, child.right, False)
        
        dfs(new_root, new_root.right, False)

        return new_root.right
        
