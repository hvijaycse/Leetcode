from typing import Any, Dict, List, Optional

def int_input()-> int:
    '''used for integer input'''
    return(int(input()))

def list_input( seperator: str = ' ')-> List:
    '''used for list input in a line seperated by seperator'''
    return input().split(seperator)

def int_list_input(seperator: str = ' ') -> List[int]:
    '''Used to get integer list in a line'''
    return list( map(int, list_input(seperator)))

def item_counter(items: List[Any]) -> Dict:
    '''
    used to get the frequency of all the item in a list
    '''
    item_count = {}

    for item in items:
        if item not in item_count:
            item_count[item] = 1
        else:
            item_count[item] += 1
    return item_count

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        

        rows = len(obstacleGrid)
        columns = len(obstacleGrid[0])

        # First filiing the first row

        if obstacleGrid[0][0] ==1:
            return 0 

        obstacleGrid[0][0] = 1
        assign = 1
        for index in range(1,columns):
            if obstacleGrid[0][index] == 1:
                obstacleGrid[0][index] = -1
                assign = -1
            obstacleGrid[0][index] = assign
        
        assign = 1
        for index in range(1, rows):
            if obstacleGrid[index][0] == 1:
                obstacleGrid[index][0] = -1
                assign = -1

            obstacleGrid[index][0] = assign
        

        for r in range(1, rows):
            for c in range(1, columns):

                if obstacleGrid[r][c] == 1:
                    obstacleGrid[r][c] = -1
                    continue
                upper = obstacleGrid[r-1][c]
                left = obstacleGrid[r][c-1]

                upper = max(upper, 0)
                left = max(left, 0)

                obstacleGrid[r][c] = upper + left
        
        return max(obstacleGrid[rows-1][columns -1], 0)