from typing import List, Optional, Any, Dict


class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        
        buses.sort()
        passengers.sort()

        i = 0 
        j = 0 

        while i < len(buses) - 1:
            current = capacity
            # print('BUS', buses[i])
            while current > 0 and j < len(passengers) -1 and passengers[j] <= buses[i]:
                # print('PASSENGER', passengers[j])
                j += 1
                current -= 1
            
            i += 1
        
        # print('BUS', buses[i])
        while capacity > 0 and j < len(passengers) and passengers[j] <= buses[i]:
            # print('PASSENGER', passengers[j])
            j += 1
            capacity -= 1
        j -= 1
        if capacity>0:
            last = buses[i]
            while j >-1 and passengers[j] == last:
                j -= 1
                last -= 1
            j += 1
            return passengers[j] - 1
        # print('PASSENGER', passengers[j])
        # print('--') 
        while j > 0 and passengers[j-1] + 1 == passengers[j]:
            # print('PASSENGER', passengers[j])
            j -=1
        
        
        return passengers[j] -1

ans = Solution().latestTimeCatchTheBus(
    [10,20],
    [2,17,18,19],
    2
)

# print(ans)