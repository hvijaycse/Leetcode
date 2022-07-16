from typing import List, Optional, Any, Dict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root is None:
            return []

        ans = []
        queue = [root]
        leftToRight = True

        while queue:

            length = len(queue)

            this_level=[]

            for index in range(length):
                current = queue[index]
                this_level.append(current.val)

                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            
            if not leftToRight:
                this_level = this_level[::-1]

            ans.append(this_level)
            leftToRight = not leftToRight
            queue = queue[length:]
        
        return ans
        



                    