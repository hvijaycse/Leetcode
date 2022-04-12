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
    def generateMatrix(self, n: int) -> List[List[int]]:

        matrix = [[0 for _ in range(n)] for _ in range(n)]
        prev = -1
        rows = n
        item = 1
        while n>0:
            for _ in range(n):
                prev += 1
                matrix[prev//rows][prev%rows] = item 
                item += 1
            
            for _ in range(n-1):
                prev += rows
                matrix[prev//rows][prev%rows] = item 
                item += 1
            
            for _ in range(n-1):
                prev -= 1
                matrix[prev//rows][prev%rows] = item 
                item += 1
            
            for _ in range(n-2):
                prev -= rows
                matrix[prev//rows][prev%rows] = item 
                item += 1
            
            n -= 2
        
        return matrix