from typing import List, Optional, Any, Dict
from functools import lru_cache

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        self.prices = prices
        return self.foo(len(prices)-1)
    
    @lru_cache(None)
    def foo(self, day):

        if day == 0 :
            return 0

        profit = 0 
        sell_price = self.prices[day]

        for i in range(0, day):
            buy_price = self.prices[i]
            current_profit = max(0, sell_price-buy_price) + self.foo(i)
            profit = max(current_profit, profit)

            
        return profit

    # def maxProfit(self, prices: List[int]) -> int:
        
    #     if len(prices) == 1:
    #         return 0
        
    #     profit = 0
    #     index = 0 

    #     while index < len(prices):

    #         while index+1 < len(prices) and prices[index] > prices[index + 1]:
    #             index += 1
            
    #         buy_price = prices[index]

    #         while index + 1 < len(prices) and prices[index] < prices[index + 1]:
    #             index += 1
            
    #         sell_price = prices[index]

    #         profit += sell_price - buy_price

    #         index += 1
        
    #     return profit