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
    def maximumCandies(self, candies: List[int], k: int) -> int:
        
        total_candies = sum(candies)

        if total_candies < k:
            return 0

        per_child = total_candies // k

        candies.sort(reverse=True)

        for possiblity in range(per_child, 1, -1):
            total_possible= 0

            for candy in candies:
                if candy // possiblity:
                    total_possible += candy // possiblity
                else:
                    break
                            
            if total_possible >= k:
                return possiblity
        
        return 1
            