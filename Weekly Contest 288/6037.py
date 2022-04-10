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
    def largestInteger(self, num: int) -> int:

        num_list = [int(i) for i in str(num)]
        odd_list = []
        even_list = []
        for i in num_list:
            if i%2:
                odd_list.append(i)
            else:
                even_list.append(i)
        
        odd_list.sort(reverse=True)
        even_list.sort(reverse=True)

        even_index = 0
        odd_index = 0

        for index, val in enumerate(num_list):

            if val % 2:
                num_list[index] = odd_list[odd_index]
                odd_index += 1
            else:
                num_list[index] = even_list[even_index]
                even_index += 1
        
        return int(''.join([ str(i) for i in num_list] ))
            