from typing import Any, Dict, List, Optional
from unicodedata import digit

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
    def plusOne(self, digits: List[int]) -> List[int]:
        
        last_index = len(digits) - 1
        carry = 1

        while last_index > -1:
            digits[last_index] += carry
            carry = digits[last_index] // 10
            digits[last_index] %= 10
            last_index -=1
            if carry == 0:
                break
        
        if carry != 0:
            digits.insert(0,carry)
        
        return digits

        

