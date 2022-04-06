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
    def correct_index(self, nums: List[int], start: int, end: int, target: int):

        while start < end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                end = mid
            else:
                start = mid + 1
        return start
          
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        if not candidates:
            return []

        candidates.sort()
        length = len(candidates)
        starting_index = self.correct_index(candidates, 0, length,target )

        if candidates[starting_index] > target:
            starting_index -= 1
        
        answer = []

        while starting_index > -1:

            current_index = starting_index
            current_target = target
            ans = []
            print('----')
            while current_target:
                item = candidates[current_index]
                times = current_target // item
                remainder = current_target % item
                ans += [item] * times


                print(current_target, item, times, remainder )
                current_target = remainder 


                if current_target== 0:
                    break

                current_index = self.correct_index(candidates, 0, current_index, current_target)

                if candidates[current_index] > current_target:
                    current_index -= 1

                if current_index < 0:
                    break
            if current_target == 0:
                answer.append(ans)
            print()

            starting_index -= 1
        return answer