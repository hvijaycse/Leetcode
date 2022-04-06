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
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        

        # Brute force approch

        for row in board:

            temp_set = set()

            for key in row:
                if key == ".":
                    continue

                if key in temp_set:
                    print("Row Failed ", key)
                    return False
                temp_set.add(key)
            
        for c in range(9):
            column = [board[r][c] for r in range(9)]
            temp_set = set()

            for key in column:
                if key == ".":
                    continue

                if key in temp_set:
                    print("colum Failed ", key)
                    return False
                temp_set.add(key)
        
        for r in range(0,9,3):
            for c in range(0,9,3):
                small = board[r: r + 3]
                temp_set = set()
                for row in small:
                    for key in row[c: c + 3]:
                        if key == ".":
                            continue
                        if key in temp_set:
                            print("small Failed ", key)
                            return False
                        temp_set.add(key)
        return True