from typing import List, Optional, Any, Dict
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        TC: O(n)
        SC: O(n)
        '''


        frequency = {}
        '''
        contain the frequency of each number
        {
            a: 10,
            b:20,
            c: 10
        }
        '''
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1
        
        frequency_mapping = {}

        '''
        contain the numbers having same frequency
        as a list
        {
            -10: [a,c],
            -20: [b]
        }

        using negative frequency as min heap will be used
        '''

        for num , freq in frequency.items():
            freq *= -1
            if freq not in frequency_mapping:
                frequency_mapping[freq] = []
            
            frequency_mapping[freq].append(num)
        
        heap = list(frequency_mapping.keys())

        # Creating a heap of top frequency 
        # This work in O(n) time
        heapq.heapify(heap)

        answer = []

        # Selecting the top k frequecny values
        while k:
            top_freq = heapq.heappop(heap)
            top_freq_number = frequency_mapping[top_freq] 
            answer += top_freq_number

            k -= len(top_freq_number)
        

        return answer