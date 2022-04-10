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
    def minimizeResult(self, expression: str) -> str:
        
        # for i, v in enumerate(expression):
        #     print(v, i , end=' |')
        # print()
        val = eval(expression)
        answer = '(' + expression + ')'
        index_of_plus = expression.index('+')
        length = len(expression)
        for open in range(0, index_of_plus):
            for close in range(index_of_plus + 2, length+1):

                a = expression[0:open]
                b = eval(expression[open:close])
                c = expression[close: ]
                # print(open, close, a , b, c)
                if a == '':
                    a = 1
                else:
                    a = int(a)
                if c == '':
                    c = 1
                else:
                    c = int(c)
                temp = a*b*c
                if temp < val:
                    val = temp
                    answer = expression[0:open] + '(' + expression[open:close] + ')' + expression[close: ]
        
        return answer

print(Solution().minimizeResult("5+22"))