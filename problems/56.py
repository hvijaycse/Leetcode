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
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        overlappings = []

        intervals.sort(key= lambda x: x[0])

        index = 0 

        while index < len(intervals):

            starting = intervals[index][0]
            ending  = intervals[index][1]

            while index < len(intervals) and intervals[index][0] <= ending:
                ending = max(intervals[index][1], ending)
                index += 1
            
            overlappings.append(
                [starting, ending]
            )
        
        return overlappings
# print(Solution().merge(  [[1,4],[4,5]]))
