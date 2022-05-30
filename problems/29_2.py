from typing import List, Optional, Any, Dict

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        answer = 0 
        times = 1
        positive = not (dividend > 0) ^ (divisor > 0)

        dividend = abs(dividend)
        divisor = abs(divisor)

        main_divisor = divisor

        while main_divisor < dividend:
            main_divisor = main_divisor << 1
            times = times << 1
        
        while dividend >= divisor:

            if main_divisor > dividend:
                main_divisor = main_divisor >> 1
                times = times >> 1
            else:
                dividend -= main_divisor
                answer += times
        
        if not positive:
            answer *= -1
        
        return min(max(-2147483648, answer), 2147483647)