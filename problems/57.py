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
    def BinaryLTE(self, start, end, nums, target ):

        while start < end:
            
            mid = (start + end) // 2

            if nums[mid][0] == target:
                return mid
            elif nums[mid][0] > target:
                end = mid
            else:
                start = mid + 1
        
        return start 
    
    def overlapping(self, intervals):

        new_interval = []

        index = 0 
        
        while index < len(intervals):

            start = intervals[index][0]
            end = intervals[index][1]

            while index < len(intervals) and intervals[index][0] <= end:
                end = max(intervals[index][1], end)
                index += 1
            new_interval.append([start, end])

        return new_interval 

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        index = self.BinaryLTE(0, len(intervals),  intervals ,newInterval[0])
        print(index)
        intervals.insert(index, newInterval)
        print(intervals)

        return self.overlapping(intervals)
