from typing import List, Optional, Any, Dict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        
        height = self.getHeight(root)

        rows = height
        columns =  (2 ** height) - 1
        matrix = [
            ['']*columns for _ in range(rows)
        ]

        self.updateMatrix(0, columns//2, root, matrix)

        return matrix

    def updateMatrix(self, row, column, root, matrix):
        
        if root is None:
            return
        
        matrix[row][column] = root.val

        self.updateMatrix(row+1, column-1, root.left, matrix)
        self.updateMatrix(row+1, column+1, root.right, matrix)

        return

    def getHeight(self, root):
        
        if root is None:
            return 0
        return 1 + max(self.getHeight(root.left), self.getHeight(root.right))