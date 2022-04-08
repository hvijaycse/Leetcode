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
    def myPow(self, x: float, n: int) -> float:
        
        answer = 1

        temp = abs(n)

        while temp:

            if temp % 2 == 1:
                answer *= x
                temp -= 1
            else:
                x = x ** 2
                temp = temp // 2
        
        if n < 0:
            return 1/answer
        return answer
        