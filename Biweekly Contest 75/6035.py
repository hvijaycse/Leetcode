from itertools import count
from typing import List, Optional

def int_input()-> int:
    '''used for integer input'''
    return(int(input()))

def list_input( seperator: str = ' ')-> List:
    '''used for list input in a line seperated by seperator'''
    return input().split(seperator)

def int_list_input(seperator: str = ' ') -> List[int]:
    '''Used to get integer list in a line'''
    return list( map(int, list_input(seperator)))

class Solution:
    def numberOfWays(self, s: str) -> int:

        counter = {
            "1": 0,
            "0": 0,
            "10": 0,
            "01": 0,
            "101": 0,
            "010": 0
        }

        for item in s:
            counter[item] += 1
            if item == "1":
                counter["01"] += counter["0"]
                counter["101"] += counter["10"]
            else:
                counter["10"] += counter["1"]
                counter["010"] += counter["01"]

        return counter["101"] + counter["010"]

    # def numberOfWays(self, s: str) -> int:
        
    #     count = 0

    #     length = len(s)

    #     indexer = {
    #         "0": [],
    #         "1": []
    #     }

    #     count_list = [0 for  _ in range(length)]

    #     for index, item in enumerate(s):

    #         if item == "1":
    #             indexer["1"].append(index)
    #             for zeros in indexer["0"]:
    #                 count += count_list[zeros]
                
    #             count_list[index] = len(indexer["0"])
    #         else:
    #             indexer["0"].append(index)
    #             for ones in indexer["1"]:
    #                 count += count_list[ones]
                
    #             count_list[index] = len(indexer["1"])
    #         # print(count_list)
        
    #     return count

# print(Solution().numberOfWays("101010"))