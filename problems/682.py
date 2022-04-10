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
    def calPoints(self, ops: List[str]) -> int:
        
        scores = []

        for operation in ops:
            try:
                operation = int(operation)
                scores.append(operation)
            except:
                if operation == "+":
                    scores.append(
                        scores[-1] + scores[-2]
                    )
                elif operation == 'D':
                    scores.append(scores[-1]*2)
                else:
                    scores.pop()
        
        return sum(scores)
