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
    def maximum_subarray(self, array):
        if not array:
            return 0

        maximum = float('-inf')
        temp_max = 0

        for value in array:

            temp_max += value

            if temp_max < 0:
                temp_max = 0
            maximum = max(maximum, temp_max)
        
        return temp_max
        
    def trap(self, height: List[int]) -> int:

        length = len(height)

        index = 0 
        temp = 0 
        left_max = [0 for _ in range(length)]


        for index in range(length):
            temp = max(temp, height[index])
            left_max[index] = temp

        index = 0 
        temp = 0 
        right_max = [0 for _ in range(length)]


        for index in range(length-1, -1, -1):
            temp = max(temp, height[index])
            right_max[index] = temp
        
        diff = [0 for _ in range(length)]

        for index in range(length):
            diff[index] = min(left_max[index], right_max[index]) - height[index]

        return self.maximum_subarray(diff) 
        

