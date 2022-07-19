from typing import List, Optional, Any, Dict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class inorderIterator:

    def __init__(self, root) -> None:
        
        self.stack = []

        while root is not None:
            self.stack.append(root)
            root = root.left
    
    def next(self):
        
        if len(self.stack) == 0 :
            return None

        last_node = self.stack.pop()
        right_node = last_node.right

        while right_node:
            self.stack.append(right_node)
            right_node = right_node.left
        
        return last_node


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        iterator1 = inorderIterator(root1)
        iterator2 = inorderIterator(root2)

        answer = []

        item1 = iterator1.next()
        item2 = iterator2.next()

        while item1 is not None and item2 is not None:

            if item1.val < item2.val:
                answer.append(item1.val)
                item1 = iterator1.next()
            else:
                answer.append(item2.val)
                item2 = iterator2.next()
            
        
        while item1 is not None:

            answer.append(item1.val)
            item1 = iterator1.next()
        
        while item2 is not None:
            answer.append(item2.val)
            item2 = iterator2.next()
        
        return answer
