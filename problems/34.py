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


class Solution:
    def binarySearch(self, array: List[int], start:int ,end: int, target: int)-> int:

        while start < end:
            mid = (start + end) // 2

            if array[mid] == target:
                return mid
            elif target < array[mid]:
                end = mid
            else:
                start = mid + 1
            
        return -1

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        end = len(nums)
        check = self.binarySearch(nums, 0, end, target)
        if check == -1:
            return [-1,-1]
        else:
            # lets first fidn the starting index

            left = check

            while True:
                l = self.binarySearch(nums, 0, left, target)
                if l == -1:
                    break
                left = l
            
            right = check

            while True:
                r = self.binarySearch(nums, right + 1, end, target)
                if r == -1:
                    break
                right = r
            
            return [left, right]



# print(Solution().searchRange([5,7,7,8,8,10], 7))