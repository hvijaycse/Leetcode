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
    def sortEvenOdd(self, nums: List[int]) -> List[int]:

        length = len(nums)

        odd = [nums[i] for i in range(1,length, 2 )]
        even = [nums[i] for i in range(0,length, 2 )]

        odd = sorted(odd, reverse=True)
        even = sorted(even)

        index = 0 
        for i in range(1, length, 2):
            nums[i] = odd[index]
            index += 1
        index = 0

        for i in range(0, length, 2):
            nums[i] = even[index]
            index += 1
            
        return nums