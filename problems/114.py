# Definition for a binary tree node.
from tracemalloc import start


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        self.myflatten(root)

    def myflatten(self, root):

        if root is None:
            return (None, None)
        
        if root.left is None and root.right is None:
            return (root, root)
        

        starting = root
        leftRoot = root.left
        rightRoot = root.right

        if leftRoot: 
            # print('left', leftRoot.val)
            lStart, lEnd = self.myflatten(leftRoot)
            root.left = None
            root.right = lStart
            root = lEnd

        if rightRoot:
            # print('right', rightRoot.val)
            rStart, rEnd = self.myflatten(rightRoot)
            root.left = None
            root.right = rStart
            root = rEnd

        # print(starting.val, root.val)
        return (starting, root)
