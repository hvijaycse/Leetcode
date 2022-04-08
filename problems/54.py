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
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        st_column = 0
        ed_column = len(matrix[0])

        st_row = 0
        ed_row = len(matrix)
        total_element = ed_column * ed_row

        answer = [ 0 for _ in range(total_element)]
        i = 0 

        while True:
            for index in range(st_column, ed_column):
                answer[i] = matrix[st_row][index]
                i += 1

            if i == total_element:
                break
            
            st_row += 1

            for index in range(st_row, ed_row):
                answer[i] = matrix[index][ed_column-1]
                i += 1

            if i == total_element:
                break
            
            ed_column -=1

            for index in range(ed_column-1, st_column-1, -1 ):
                # print(answer, ed_row-1, index)
                answer[i] = matrix[ed_row-1][index]
                i += 1

            if i == total_element:
                break
            

            ed_row -= 1

            for index in range(ed_row -1, st_row-1, -1):
                answer[i] = matrix[index][st_column]
                i += 1
            st_column += 1
                    
        return answer

print(Solution().spiralOrder( [[1,2,3,4],[5,6,7,8],[9,10,11,12]]))