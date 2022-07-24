from typing import List, Optional, Any, Dict

class SegmentTree:

    def __init__(self, nums: List[int]) -> None:
        self.original = list(nums)
        self.length = len(nums)
        self.tree = [0] * (4 * self.length)
        self.identity = 0

        self._buildTree(0, self.length -1, 0)

    def left(self, index: int):
        return 2 * index + 1

    def right(self, index: int):
        return 2 * ( index + 1)
        
    def operator(self, a: int, b: int) -> int:
        return a + b
    
    def _buildTree(self, ragneL, rangeR, curr):

        if ragneL == rangeR:
            self.tree[curr] = self.original[ragneL]
            return
        

        mid = (ragneL + rangeR) // 2

        self._buildTree(ragneL, mid, self.left(curr))
        self._buildTree(mid + 1, rangeR, self.right(curr))

        self.tree[curr] = self.operator(
            self.tree[self.left(curr)], 
            self.tree[self.right(curr)]
            )

        return
    
    def sumRange(self, left: int, right: int):
    
        return self._sumRange(0, self.length -1, left, right, 0)

    def _sumRange(self, rLeft: int, rRight: int, qLeft: int, qRight: int, curr: int) -> int:
        
        if qLeft <= rLeft <= rRight <= qRight:
            return self.tree[curr]
        
        if rRight < qLeft or qRight < rLeft:
            return self.identity
        
        mid = (rLeft + rRight) // 2

        leftVal = self._sumRange(rLeft, mid, qLeft, qRight, self.left(curr))
        rightVal = self._sumRange(mid + 1, rRight, qLeft, qRight, self.right(curr))

        return self.operator(leftVal, rightVal)
    
    def update(self, index: int, val: int):   
        self._update(index, 0, self.length -1, 0, val )

    def _update(self, index:int, left:int, right:int, curr:int, val:int):

        if left == right:
            self.tree[curr] = val
            return
        
        mid  = (left + right) // 2

        if index <= mid:
            self._update(index, left, mid, self.left(curr), val )
        else:
            self._update(index, mid + 1, right, self.right(curr), val)
        

        self.tree[curr] = self.operator(
            self.tree[self.left(curr)], 
            self.tree[self.right(curr)]
            )
    

class NumArray:

    def __init__(self, nums: List[int]):
        self.myTree = SegmentTree(nums)
                

    def update(self, index: int, val: int) -> None:
        self.myTree.update(index, val)
        

    def sumRange(self, left: int, right: int) -> int:
        return self.myTree.sumRange(left, right)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
