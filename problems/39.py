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
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        

        def combination( start: int, end: int, target: int, path: List[int]):
            if start == end:
                return
            else:

                for index in range(start, end):

                    val = candidates[index]
                    new_target = target - val

                    if new_target < 0:
                        break
                    elif new_target == 0:
                        answers.append(
                            list(path) + [val]
                        )
                        break
                    else:
                        path.append(val)
                        combination(index, end, new_target, path)
                        path.pop()
        
        answers = []
        candidates.sort()
        combination(0, len(candidates), target, [] )

        return answers