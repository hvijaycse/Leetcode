from multiprocessing.dummy import current_process
from typing import List, Optional, Any, Dict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.add_node(root)
        
    def next(self) -> int:
        item: TreeNode = self.stack.pop()
        self.add_node(item.right)
        return item.val

    def hasNext(self) -> bool:
        return len(self.stack)> 0
        

    def add_node(self, node):
        while node:
            self.stack.append(node)
            node = node.left


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()