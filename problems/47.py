import re
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
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        total_combinations = []
        nums.sort()
        self.dfs(
            total_combinations, nums
        )

        return total_combinations
    
    def dfs(self, combinations, array):

        if len(array) == 1:
            combinations.append(array)
        else:

            index = 0 
            end = len(array)
            while index < end:
                val = array[index]
                val_combi = []
                temp_array = [i for i in array]
                temp_array.pop(index)
                self.dfs(val_combi, temp_array )

                for comb in val_combi:
                    if comb:
                        combinations.append(
                            [val] + comb
                        )
                
                while index < end and array[index] == val:
                    index += 1
                    
        

