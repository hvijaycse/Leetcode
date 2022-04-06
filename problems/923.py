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
    def threeSumMulti(self, arr: List[int], target: int) -> int:

        arr.sort()
        total_count = 0
        l = len(arr)

        for i in range(l-2):

            temp_target = target - arr[i]

            j = i + 1
            k = l - 1

            while j < k:

                if arr[j] + arr[k] < temp_target:
                    j += 1
                elif arr[j] + arr[k] > temp_target:
                    k -= 1
                elif arr[j] != arr[k]:

                    left = right = 1
                    while j + 1< k and arr[j] == arr[j+1]:
                        j += 1
                        left += 1
                    
                    while k  -1> j and arr[k] == arr[k-1]:
                        k -= 1
                        right  += 1

                    total_count += left * right
                    j += 1
                    k -= 1
                else:
                    n = k - j + 1
                    total_count += n*(n-1)//2
                    break
        return total_count % 1000000007

                            

