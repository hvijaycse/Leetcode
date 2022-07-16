from typing import List, Optional, Any, Dict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        answer = []
        self.postOrder([root], answer)
        return answer

    def postOrder(self, level, answer):
        
        next_level = []
        current_level = []

        for node in level: 

            if node is None:
                continue

            current_level.append(node.val)
            if node.left: next_level.append(node.left)
            if node.right: next_level.append(node.right)
        
        if next_level:
            self.postOrder(next_level, answer)
        if current_level:
            answer.append(current_level)

        return answer
