from os import pathsep
from typing import List, Optional, Any, Dict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def __init__(self) -> None:
        self.paths = []

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        self.dfs(root, targetSum,[])

        return self.paths

    def dfs(self, root: TreeNode, targetSum: int , currentPath: List):

        if root is None:
            return

        currentPath.append(root.val)
        targetSum = targetSum - root.val

        if root.left is None and root.right is None and targetSum == 0:
            self.paths.append(list(currentPath))
        
        if root.left:
            self.dfs(root.left, targetSum, currentPath)
        
        if root.right:
            self.dfs(root.right, targetSum, currentPath)
        
        currentPath.pop()
        

