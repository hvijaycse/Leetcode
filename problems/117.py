import queue
from typing import List, Optional, Any, Dict


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':

        if not root:
            return
        else:

            current_level = [root]

            while current_level:
                next_level = []
                for index in range(0, len(current_level)-1):
                    current_level[index].next = current_level[index+1]
                    if current_level[index].left:
                        next_level.append(current_level[index].left)

                    if current_level[index].right:
                        next_level.append(current_level[index].right)
                if current_level[-1].left:
                    next_level.append(current_level[-1].left)

                if current_level[-1].right:
                    next_level.append(current_level[-1].right)
                current_level = next_level
        
        return root