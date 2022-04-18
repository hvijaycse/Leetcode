from platform import node
from typing import List, Optional, Any, Dict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def search(root: TreeNode, count: List[int]) -> TreeNode:

            if not root:
                return None
            else:
                answer = search(root.left, count)
                
                if answer != None:
                    return answer

                count[0] += 1

                if count[0] == k:
                    return root
                else:
                    return search(root.right, count)

        node = search(root,[0])

        return node.val


