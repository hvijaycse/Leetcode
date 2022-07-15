from typing import List, Optional, Any, Dict


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):

        self.stack = []
        while root:
            self.stack.append(root)        
            root = root.left

    def next(self) -> int:
        
        root = self.stack.pop()
        root_right = root.right
        while root_right:
            self.stack.append(root_right)
            root_right = root_right.left
        
        return root.val

    def hasNext(self) -> bool:

        return len(self.stack) > 0        

