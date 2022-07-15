from typing import List, Optional, Any, Dict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):

        self.queue = [root]
        self.root = root
                

    def insert(self, val: int) -> int:
        newNode = TreeNode(val)

        while True:

            current = self.queue[0]

            if current.left is None:
                current.left = newNode
                break
            elif current.right is None:
                current.right = newNode
                break
            else:
                self.queue.append(current.left)
                self.queue.append(current.right)
                self.queue.pop(0)
        
        return self.queue[0].val

        
        

    def get_root(self) -> Optional[TreeNode]:
        return self.root
        


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()
