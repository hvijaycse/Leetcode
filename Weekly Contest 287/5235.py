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
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        

        losser_count = {}
        winners = set()
        lossers = set()


        for match in matches:
            winner , losser = match

            losser_count[losser] = losser_count.get(losser,0) + 1

            winners.add(winner)
            lossers.add(losser)

        
        first = list(winners - lossers)

        second = []

        for losser in losser_count:
            if losser_count[losser] == 1:
                second.append(losser)
        
        first.sort()
        second.sort()

        return [first, second]
        