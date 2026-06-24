class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # goal: want to find argmax(prices[j] - prices[i]),
        # where j > i
        # store running max, min seen
        # we can do any trade s.t. max - min
        min_price = float('inf')
        profit = 0
        for p in prices:
            sale = p - min_price
         #   max_price = max(p, max_price)
           # min_price = min(p, min_price)
            profit = max(sale, profit)
            min_price = min(p, min_price)

        
        return profit
