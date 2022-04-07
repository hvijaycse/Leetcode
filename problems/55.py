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
    def canJump(self, nums: List[int]) -> bool:
        """
        basic logic is that 
        if are not able to walk then break otherwise
        increase the counter for reached as we have covered 
        one more block
        """

        can_walk = nums[0]
        length = len(nums)
        reached = 1

        for index in range(1, length):

            if can_walk == 0:
                break
            can_walk = max(nums[index], can_walk-1)
            reached += 1
        
        return reached == length
