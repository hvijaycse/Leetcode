from distutils.command.config import config
from importlib.util import resolve_name
from typing import List, Mapping, Optional

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
    def romanToInt(self, s: str) -> int:
        

        Roman_to_int = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }

        conditions = {
            'I':{
                'V': 4,
                'X': 9
            },

            'X':{
                'L': 40,
                'C': 90
            },

            'C':{
                'D': 400,
                'M': 900
            }
        }


        number = 0
        index = 0
        length = len(s)


        while index < length:

            if s[index] in conditions and index < length - 1:

                if s[index + 1] in conditions[s[index]]:
                    number += conditions[s[index]][s[index + 1]]
                    index += 2
                else:
                    number += Roman_to_int[s[index]]
                    index += 1
            else:
                number += Roman_to_int[s[index]] 
                index += 1
        
        return number