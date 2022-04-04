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
    def minBitFlips(self, start: int, goal: int) -> int:

        diff = start ^ goal
        return bin(diff).count('1')

# class Solution:
#     def minBitFlips(self, start: int, goal: int) -> int:

#         if start == goal:
#             return 0 

#         flip_count = 0

#         start_bin = f"{start:b}"[::-1]
#         goal_bin = f"{goal:b}"[::-1]

#         goal_len=len(goal_bin)        
#         start_len=len(start_bin)        

#         if start_len < goal_len:

#             for index in range(start_len):

#                 if start_bin[index] != goal_bin[index]:
#                     flip_count += 1
#             for index in range(start_len, goal_len):
#                 if goal_bin[index] == "1":
#                     flip_count += 1
#         else:

#             for index in range(goal_len):

#                 if start_bin[index] != goal_bin[index]:
#                     flip_count += 1
            
#             for index in range(goal_len, start_len):
#                 if start_bin[index] == '1':
#                     flip_count += 1
#         return flip_count

