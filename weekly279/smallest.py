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
    def smallestNumber(self, num: int) -> int:

        if num < 0 :
            num  *= -1 
            nums = [ i for i in str(num)]
            nums.sort(reverse=True)
            ans = -int(''.join(nums))

        else:
            
            nums = [ i for i in str(num)]
            nums.sort()

            length = len(nums)
            index = 0 

            while index < length and nums[index] == '0':
                index += 1

            if index < length:
                nums[index], nums[0] = nums[0], nums[index]
            
            ans = int(''.join(nums))
        return ans