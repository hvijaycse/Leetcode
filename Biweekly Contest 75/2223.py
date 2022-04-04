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

    def z_function(self, s: str) -> List[int]:
        length = len(s)

        z = [0]* length
        l = r = 0

        for index in range(1, length):

            if index <= r:
                z[index] = min(r-index + 1, z[index-l])
            
            while index + z[index] < length and s[index + z[index]] == s[z[index]]:
                z[index] += 1
            
            if index + z[index] - 1> r:
                r = index + z[index]-1
                l = index
        
        return z

    def sumScores(self, s: str) -> int:

        return sum(self.z_function(s)) + len(s)
        