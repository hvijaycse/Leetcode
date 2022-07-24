import re
from typing import List, Optional, Any, Dict

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        
        buckets = {}
        width = t + 1

        for index, num in enumerate(nums):

            bucket_i = num // width
            bucket_low = bucket_i - 1
            bucket_high = bucket_i + 1
            
            if bucket_i in buckets: 
                return True

            if bucket_low in buckets and abs(buckets[bucket_low] - num) <= t:
                return True 

            if bucket_high in buckets and abs(buckets[bucket_high] - num) <= t:
                return True 
            
            buckets[bucket_i] = num

            if index >= k:
                del buckets[nums[index - k] // width]

        return False 