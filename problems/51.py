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
    def solveNQueens(self, n: int) -> List[List[str]]:
        

        def bfs(i):

            if i == n:
                boards.append(list(board))
            else:
                for j in range(n):

                    if (
                        j not in column 
                        and i + j not in off_daig 
                        and j-i not in daig
                    ):
                        column.add(j)
                        off_daig.add(i +j)
                        daig.add(j-i)

                        board.append(
                            '.'*j + 'Q' + '.'*(n-j -1)
                        )

                        bfs(i + 1)
                        board.pop()
                        column.remove(j)
                        off_daig.remove(i + j)
                        daig.remove(j-i)
            
        boards = []
        board = []
        column = set()
        off_daig = set()
        daig = set()
        bfs(0)

        return boards
