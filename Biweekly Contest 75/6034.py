from typing import List, Optional

def int_input()-> int:
    '''used for integer input'''
    return(int(input()))

def list_input( seperator: str = ' ')-> List:
    '''used for list input in a line seperated by seperator'''
    return input().split(seperator)

def int_list_input(seperator: str = ' ') -> List[int]:
    '''Used to get integer list in a line'''
    return list( map(int, list_input(seperator)))

class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        
        n = len(nums)

        for last in range(1, n):

            for index in range(0, n-last):
                nums[index] += nums[index + 1]
                nums[index] %= 10
            
        return nums[0]