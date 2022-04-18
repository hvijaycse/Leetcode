from typing import List, Optional, Any, Dict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:


        def dfs(root: TreeNode, parent: TreeNode, is_Left: bool  ) -> None:
            
            if not root:
                return
            else:
                dfs(root.left, root, True)
                dfs(root.right, root, False)
                if is_Left:
                    if root.left:
                        left_node = root.left
                        root.left = None
                        parent.left = left_node
                        
                        while left_node.right:
                            left_node = left_node.right

                        left_node.right = root

                else:
                    if root.left:
                        left_node = root.left
                        root.left = None
                        parent.right = left_node
                        while left_node.right:
                            left_node = left_node.right
                        left_node.right = root
        
        new_root = TreeNode(-1, None, right=root)
        dfs(new_root.right, new_root, False )

        return new_root.right