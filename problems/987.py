from typing import List, Optional, Any, Dict


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        mapping = {}

        self.dfs(root, 0, mapping)

        answer = []

        for index in sorted(mapping.keys()):
            answer.append(mapping[index])
        
        return answer

    
    def dfs(self, root, index, mapping):

        if not root:
            return
        
        if index not in mapping:
            mapping[index] = []
        
        mapping[index].append(root.val)

        self.dfs(root.left, index-1, mapping)
        self.dfs(root.right, index+1, mapping)

