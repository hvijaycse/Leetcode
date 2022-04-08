from typing import Any, Dict, List, Optional

def int_input()-> int:
    '''used for integer input'''
    return(int(input()))

def list_input( seperator: str = ' ')-> List:
    '''used for list input in a line seperated by seperator'''
    return input().split(seperator)

def int_list_input(seperator: str = ' ') -> List[int]:
    '''Used to get integer list in a line'''
    return list( map(int, list_input(seperator)))

def item_counter(items: List[Any]) -> Dict:
    '''
    used to get the frequency of all the item in a list
    '''
    item_count = {}

    for item in items:
        if item not in item_count:
            item_count[item] = 1
        else:
            item_count[item] += 1
    return item_count


class KthLargest:
    def BinaryLTE(self, start, end, nums, target) :

        while start < end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                end = mid
            else:
                start = mid + 1
        
        return start

    def __init__(self, k: int, nums: List[int]):

        self.k = k
        self.nums = nums
        self.nums.sort()
        self.length = len(nums)

        

    def add(self, val: int) -> int:

        index_for_val = self.BinaryLTE(0, self.length, self.nums, val)
        self.nums.insert(index_for_val, val)
        self.length += 1
        return self.nums[-self.k]

        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)