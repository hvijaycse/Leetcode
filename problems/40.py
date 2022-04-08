from ctypes.wintypes import tagRECT
from typing import Any, Dict, List, Optional

from idna import valid_contextj

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
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        def bfs(i: int, max: int, target: int , path: List[int]):
            # print(i, target)
            if i == max:
                return 
            else:
                index = i
                for index in range(i, max):

                    if index > i and candidates[index] == candidates[index - 1]:
                        continue
                    val = candidates[index]
                    new_target = target - val
                    if new_target < 0:
                        continue
                    if new_target == 0:
                        answers.append(list(path) + [val])
                    else:
                        path.append(val)
                        bfs(index+1, max, new_target, path)
                        path.pop()
        answers = []
        candidates.sort()
        bfs(0, len(candidates), target, [])

        return answers


print(Solution().combinationSum2([10,1,2,7,6,1,5],8))