from ctypes.wintypes import tagRECT
from typing import Any, Dict, List, Optional

from idna import valid_contextj

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
    def BinaryLTE(self, start: int,end: int, nums: List[int], target: int) -> int:

        while start < end:
            mid = (start + end) // 2

            if nums[mid] == target:
                return mid
            
            elif target < nums[mid]:
                end = mid
            else:
                start = mid + 1
        
        return start - 1

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Not solved
        """
        
        candidates.sort()
        answers = []
        self.bfs(candidates, 0, len(candidates), target, answers)

        return answers
    
    def bfs(self, candidates: List[int], start: int, end: int, target: int, path: List[List[int]]) -> None:

        if target < 0:
          return
        
        for index in range(start, end):

            val = candidates[index]

            diff = target - val

            if diff == 0:
                if [val] not in path:
                    path.append([val])
            else:
                path_for_diff = []

                self.bfs(candidates, index + 1, end, diff, path_for_diff)

                if path_for_diff:
                    for p in path_for_diff:
                        temp = [val] + p
                        if temp not in path:
                            path.append(temp)
                    