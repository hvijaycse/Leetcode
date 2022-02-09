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
    def divide(self, dividend: int, divisor: int) -> int:

        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        
        dividend_pos = dividend >= 0
        divisor_pos = divisor >= 0 

        answer_pos = divisor_pos == dividend_pos

        dividend = abs(dividend)
        divisor = abs(divisor)
        
        answer = 0

        temp_divisor = divisor
        times = 1

        while dividend >= temp_divisor * 2:
            times *= 2
            temp_divisor *= 2

        while temp_divisor >= divisor:
            if dividend >= temp_divisor:
                dividend -= temp_divisor
                answer += times
            else:
                temp_divisor = temp_divisor // 2
                times = times // 2
        
        if not answer_pos:
            answer = - answer
        return answer 