from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        

        def binary(lo: int, hi: int) -> bool:

            while lo < hi:
                
                mid = (lo + hi) // 2

                if nums[mid] == target:
                    return True

                elif nums[lo] < nums[mid]:
         
                    if nums[lo] <= target < nums[mid]:
                        hi = mid 
                    else:
                        lo = mid + 1
                elif nums[lo] > nums[mid]:
                    if nums[mid] < target <= nums[hi-1]:
                        lo = mid + 1
                    else:
                        hi = mid 
                else:
                    return binary(lo, mid) or binary(mid+1 , hi)
            else:
                return False

        return binary(0, len(nums))
    
# print(Solution().search([1,3,1,1,1,1,1], 3))