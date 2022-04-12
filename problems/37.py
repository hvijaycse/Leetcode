from pkgutil import iter_modules
from typing import Any, Dict, List, Optional
from unicodedata import numeric

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
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        rows_set = [set() for _ in range(9)]

        for index, row in enumerate(board):

            for item in row:
                if item != '.':
                    rows_set[index].add(item)
        
        column_set = [set() for _ in range(9)]

        for column in range(9):
            for row in range(9):
                for item in board[row][column]:
                    if item != '.':
                        column_set[column].add(item)
        
        smaller = [ [set(), set(), set()] for _ in range(3)]

        for index in range(81):
            item = board[index//9][index%9]

            if item!='.':
                smaller[index//27][(index%9)//3].add(item)
        

        def bfs(num: int, board: List[List[str]]):

            if num == 81:
                return True
            
            row = num // 9 
            column = num % 9

            if board[row][column] != '.':
                return bfs(num + 1, board)
            else:

                for number in range(1, 10):
                    number = str(number)

                    if number not in rows_set[row] and number not in column_set[column] and number not in smaller[row//3][column//3]:
                        board[row][column] = number
                        rows_set[row].add(number)
                        column_set[column].add(number)
                        smaller[row//3][column//3].add(number)

                        possible = bfs(num + 1, board )
                        if possible:
                            return True
                        board[row][column] = '.' # This stupid update is really important otherwise the if at line 69 will skip it.
                        rows_set[row].remove(number)
                        column_set[column].remove(number)
                        smaller[row//3][column//3].remove(number)
                return False
                               


        bfs(0, board)

