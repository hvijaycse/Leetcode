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
    def search(self, nums: List[int], target: int) -> int:

        start = 0 
        end = len(nums)


        while start < end:

            mid = (start + end) // 2


            if nums[mid] == target:
                return mid
            

            elif nums[start] < nums[mid]:

                if nums[start] <= target < nums[mid]:
                    end = mid
                else:
                    start = mid + 1
            
            elif nums[start] > nums[mid]:

                if nums[mid] < target <= nums[end-1]:
                    start = mid + 1
                else:
                    end = mid
            else:
                start = mid + 1
        
        return -1 