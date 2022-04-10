from itertools import count
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
    def maximumProduct(self, nums: List[int], k: int) -> int:
        """
        Good try but TLE, never the less logic was correct
        """

        counter = {}


        for num in nums:
            if num not in counter:
                counter[num] = 1
            else:
                counter[num] += 1
        
        while k :

            minimum = min(counter.keys())
            
            count = counter[minimum]
            increase = min(k, count)

            if minimum + 1 not in counter:
                counter[minimum + 1] = increase
            else:
                counter[minimum + 1] += increase
            
            counter[minimum] -= increase

            if counter[minimum] == 0:
                del counter[minimum]
            
            k -= increase
        answer = 1
        for key, val in counter.items():
            answer *= key ** val
        mod = 1000000007

        return answer % mod
