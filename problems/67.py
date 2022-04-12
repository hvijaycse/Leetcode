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
    def addBinary(self, a: str, b: str) -> str:

        a_l, b_l = -len(a), -len(b)
        index, res, carry = -1, '', 0

        for index in range(-1, min(a_l, b_l)-1, -1):

            a_i = int(a[index]) if index >= a_l else 0
            b_i = int(b[index]) if index >= b_l else 0

            sum = a_i + b_i + carry

            res = str(sum%2) + res

            carry = sum // 2
        
        return '1' + res if carry else res
