from typing import List, Optional, Any, Dict

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

    possible, _ = findSum(root, totalSum // 2)

    return possible

def findSum(root: BinaryTreeNode, sum: int):

    if root is None:
        return (False, 0)
    
    lPossible, lSum = findSum(root.left, sum)
    rPossible, rSum = findSum(root.right, sum)

    total_sum = lSum + rSum + root.data

    possible = lPossible or rPossible or (total_sum == sum)
    
    return (possible, total_sum)
    
    

def getSum( node: BinaryTreeNode):

    if node is None:
        return  0
    
    return node.data + getSum(node.left) + getSum(node.right)

