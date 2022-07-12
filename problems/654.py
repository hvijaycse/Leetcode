from typing import List, Optional, Any, Dict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        

    #     if len(nums) == 0 :
    #         return None
        
    #     maximum = max(nums)
    #     maximum_index = nums.index(maximum)

    #     root_node = TreeNode(maximum)

        
    #     root_node.left = self.constructMaximumBinaryTree(nums[: maximum_index -1])
    #     root_node.right = self.constructMaximumBinaryTree(nums[maximum_index + 1 :])

    #     return root_node
    
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:

        root_node = TreeNode(nums[0])

        for i in range(1, len(nums)):

            new_node = TreeNode(nums[i])

            if new_node.val > root_node.val:
                new_node.left = root_node
                root_node = new_node
            else:

                self.insert_node(parent=root_node, new_node=new_node)
        
        return root_node
    

    def insert_node(self, parent: TreeNode, new_node: TreeNode):

        child: TreeNode = parent.right

        while child is not None and child.val > new_node.val:
            parent = parent.right
            child = child.right
        
        if child is not None:
            new_node.left = child

        parent.right = new_node




        

