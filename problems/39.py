from socket import if_indextoname
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

    def binaryLTE(self, start, end, array, target):

        while start < end:

            mid = (start + end) //2

            if array[mid] == target:
                return mid
            elif target < array[mid]:
                end = mid
            else:
                start += 1

        return start - 1

    def mycombination(self, candidates, target):

        Answers = []

        last_index = self.binaryLTE(0, len(candidates), candidates, target)

        for index in range(last_index + 1):
            val = candidates[index]
            temp_target = target - val

            if temp_target < 0:
                break
            elif temp_target == 0:
                Answers.append([val])
                break
            else:

                if temp_target not in self.answer_dict:
                    new_target_possible = self.combinationSum(candidates, temp_target)
                else:
                    new_target_possible = self.answer_dict[temp_target]
                if  new_target_possible:
                    for item in new_target_possible:
                        temp_answer = [val] + item
                        temp_answer.sort()
                        if temp_answer not in Answers:
                            Answers.append(temp_answer)

        self.answer_dict[target] = Answers
        return Answers
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.
        The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.
        It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
        """
        
        candidates.sort()
        self.answer_dict = {}
        return self.mycombination(candidates, target)
        


# print(Solution().combinationSum([2,2,2,2,2,2,3,3,3,3],12))