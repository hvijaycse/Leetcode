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
    def jump(self, nums: List[int]) -> int:
        
        length = len(nums)

        maximum = [item for item in nums]

        for index in range(1,length):
            maximum[index] = max(maximum[index-1]-1, maximum[index])
        
        jumps = 0 
        distance = 0 

        index = length - 1

        while index != 0:

            while index > -1 and maximum[index] >= distance:
                index -=1 
                distance += 1
            jumps += 1
            index +=1
            distance = 0
        
        return jumps

