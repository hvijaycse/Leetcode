from itertools import count
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

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        columns = len(board[0])

        def checkPosition(r,c, rows, columns):
            count = 0
            count -= board[r][c]

            start_r = max(r-1,0)
            end_r = min(r+2, rows)

            start_c = max(c-1, 0)
            end_c=  min(c+2, columns)

            for r in range(start_r, end_r):
                for c in range(start_c, end_c):
                    count += board[r][c]
            
            return count

        new_board = [[0]*columns for _ in range(rows)]

        for r in range(rows):
            for c in range(columns):
                neighbour = checkPosition(r, c, rows, columns)
                # print(f"row: {r}, column: {c}, neighbour: {neighbour}")

                if neighbour < 2:
                    new_board[r][c] = 0
                elif neighbour == 2:
                    new_board[r][c] = board[r][c]
                elif neighbour == 3:
                    new_board[r][c] = 1
                elif neighbour > 3:
                    new_board[r][c] = 0
        
        for r in range(rows):
            for c in range(columns):
                board[r][c] = new_board[r][c]


# board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
# for row in board: print(row)
# print()
# Solution().gameOfLife(board)
# for row in board: print(row)