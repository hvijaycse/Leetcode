

class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n < 4:
            return n 
        second_last , last = 2, 3
        for i in range(3, n):
            second_last, last =  last, second_last+last
        
        return last