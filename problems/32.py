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
    def longestValidParentheses(self, s: str) -> int:
        

        stack = [-1]
        max_length = 0

        for index, char in enumerate(s):

            if char == "(":
                stack.append(index)
            else:
                stack.pop()

                if not stack:
                    stack.append(index)
                else:
                    max_length = max(index - stack[-1], max_length)
        
        return max_length
        