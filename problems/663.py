from typing import List, Optional, Any, Dict

'''
This question is taken from codingNinja 
as it was premium on leetcode 
'''

# Structure of BinaryTreeNode class for reference.
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



def checkEqualTree(root):
    # Write your code here.
    # Return True or False.

    totalSum = getSum(root)

    if totalSum %2 ==1 :
        possible = False
    else:
        possible, _ = findSum(root, totalSum // 2)

    return possible

def findSum(root: BinaryTreeNode, sum: int):

    if root is None:
        return (False, 0)
    
    lPossible, lSum = findSum(root.left, sum)
    rPossible, rSum = findSum(root.right, sum)

    if lPossible:
        return (lPossible, lSum)
    elif rPossible:
        return (rPossible, rSum)

    total_sum = lSum + rSum + root.data

    return (total_sum == sum, total_sum)

def getSum( node: BinaryTreeNode):

    if node is None:
        return  0
    return node.data + getSum(node.left) + getSum(node.right)
