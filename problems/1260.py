from re import L
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
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        
        def num_to_RC(num: int, c) -> List[int]:
            return [num // c, num % c]
        
        rows = len(grid)
        column = len(grid[0])
        total_items = len(grid)*len(grid[0])

        k = k % total_items

        temp = [0 for _ in range(k)]
        for index, val  in enumerate(range(total_items -k , total_items)):
            r, c = num_to_RC(val, column)
            temp[index] = grid[r][c]
        
        for index in range(total_items - 1, k-1, -1):
            old_r, old_c = num_to_RC(index - k, column)
            new_r, new_c = num_to_RC(index, column)

            grid[new_r][new_c] = grid[old_r][old_c]
        
        for index in range(k):
            r, c = num_to_RC(index, column)
            grid[r][c] = temp[index]

        return grid
