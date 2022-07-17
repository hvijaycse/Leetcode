from typing import List, Optional, Any, Dict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        possible = False

        targetNode = self.bfs(root, x)

        leftCount = self.count(targetNode.left)
        rightCount = self.count(targetNode.right)
        parentCount = n - 1 - leftCount - rightCount

        maxVal = max(leftCount, rightCount, parentCount)

        if maxVal > n-1-maxVal:
            possible = True
        
        return possible

    def bfs(self, root: TreeNode, target: int) -> TreeNode:

        queue = [root]

        for node in queue:
            if node is None:
                continue
            if node.val == target:
                return node
            
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)

    def count(self, root):

        queue = [root]
        count = 0 
        
        for node in queue:
            if node is None:
                continue
            count += 1
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        
        return count