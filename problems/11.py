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
    def maxArea(self, height: List[int]) -> int:

        '''
        Brute force

        O(n^2)
        '''

        # max_volume = 0 
        # length = len(height)

        # for i in range(length-1):
        #     for j in range(i+1, length):

        #         max_volume = max(
        #             max_volume,
        #             min(height[i], height[j]) * (j-i)
        #         )
        
        # return max_volume

        '''
        Two pointer 
        Greddy approch
        O(n)
        '''

        max_volume = 0

        start: int = 0 
        end:int = len(height) - 1

        while start < end:

            max_volume = max(
                max_volume,
                min(height[start], height[end]) * (end - start)
            )

            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return max_volume