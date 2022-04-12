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
    def getPermutation(self, n: int, k: int) -> str:
        
        factorials = [1 for _ in range(n)]

        for i in range(1, n):
            factorials[i] = i * factorials[i-1]

        numbers = [str(i) for i in range(1, n+1)]

        answer = ''

        while k :
            if k == 1:
                answer += ''.join(numbers)
                break

            index = (k-1) // factorials[n-1]

            answer += numbers[index]

            numbers.pop(index)

            k = k % factorials[n-1]

            if k == 0:
                k = factorials[n-1]
            n -= 1 
        
        return answer
