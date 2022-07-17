from typing import List, Optional, Any, Dict

'''
In an infinite binary tree where every node has two children, the nodes are labelled in row order.

In the odd numbered rows (ie., the first, third, fifth,...), the labelling is left to right, while in the even numbered rows (second, fourth, sixth,...), the labelling is right to left.

Given the label of a node in this tree, return the labels in the path from the root of the tree to the node with that label.
'''

class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        
        temp = label //2
        level = 0 
        while temp:
            level += 1
            temp = temp // 2
        
        levelMax = 2 ** (level+1) -1
        levelMin = 2 ** level
        path = []

        self.genPath(label, levelMin, levelMax, path)

        return path[::-1]

    
    def genPath(self, label, levelMin, levelMax, path):

        path.append(label)

        if label < 2:
            return

        parent = (levelMax + levelMin - label) // 2

        self.genPath(parent, levelMin//2, levelMax//2, path)    