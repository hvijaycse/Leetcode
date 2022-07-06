from typing import List, Optional, Any, Dict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        number_dict = {}

        for num in nums:
            number_dict[num] = 0
            
        
        ans = 0 

        for num in number_dict.keys():

            if number_dict[num] == -1:
                continue

            count = 1

            low = num - 1
            while low in number_dict:
                number_dict[low] = -1
                low -= 1
                count += 1


            high = num + 1

            while high in number_dict:
                number_dict[high] = -1
                high += 1
                count += 1
            
            ans = max(ans, count)
        
        return ans
