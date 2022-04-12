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
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        columns = len(grid[0])

        for i in range(1, rows):
            grid[i][0] += grid[i-1][0]
        
        for i in range(1, columns):
            grid[0][i] += grid[0][i-1]
        
        for r in range(1, rows):
            for c in range(1, columns):
                grid[r][c]+= min(grid[r-1][c], grid[r][c-1])
        
        return grid[rows-1][columns-1]