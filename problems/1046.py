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
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        Brute force solution
        Time Complexity: O(n^2*log(n))
        Space Complexity: O(0)

        A better algorithm to sovle this problme will
        make use of maxheap data structure, will come back to this 
        after revising headp.
        
        """
        stones.sort()

        while stones:

            last_stone = stones.pop()

            if not stones:
                break

            last_stone  = last_stone - stones.pop()

            if last_stone != 0 :
                stones.append(last_stone)
                stones.sort()

        return last_stone

