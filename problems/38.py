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
    def countAndSay(self, n: int) -> str:
        saying = '1'

        for i in range(1, n):
            new_saying = ''
            
            index = 0 
            length = len(saying)

            while index < length:
                count = 0
                char = saying[index]
                while index < length and saying[index] == char:
                    index += 1
                    count += 1
                new_saying += str(count) + char

            saying = new_saying
        
        return saying
