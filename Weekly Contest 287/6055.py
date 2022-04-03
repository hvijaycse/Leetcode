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
    def convertToInt(self, time) -> int:
        hour, minute = map(int, time.split(':'))

        return hour*60 + minute

    def convertTime(self, current: str, correct: str) -> int:

        if current == correct:
            return 0 

        minimum_change = 0

        correct_int = self.convertToInt(correct)
        current_int = self.convertToInt(current)


        difference = correct_int - current_int

        for diff in [60,15,5,1]:

            if difference >= diff:
                times = difference // diff
                minimum_change += times
                difference -= diff * times
        
        return minimum_change
