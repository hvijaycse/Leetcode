from typing import List, Optional, Any, Dict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:

        parents = set()
        

        node_dict = dict()

        for (parent, child, isleft) in descriptions:

            if parent not in node_dict:
                node_dict[parent] = TreeNode(parent)

            if child not in node_dict:
                node_dict[child] = TreeNode(child)
            
            child_node = node_dict[child]
            parent_node = node_dict[parent]

            if isleft:
                parent_node.left = child_node
            else:
                parent_node.right = child_node
            
            
            parents.add(parent)
        
        for index in range(len(descriptions)):

            if descriptions[index][1] in parents:
                parents.remove(descriptions[index][1])
        
        return node_dict[parents.pop()]
        


            