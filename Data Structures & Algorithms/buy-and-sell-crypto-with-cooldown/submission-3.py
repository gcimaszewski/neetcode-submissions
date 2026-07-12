class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # records if at time t, we can buy the coin according to the rules
        # recurrence: 
        # on last day t: 
        # profit(t) = profit(t-1) + prices[t] if can sell on day t
         #             or profit(t-1) (just stay put)
        # store for an index i into prices whether we are holding the stock or not
        memo = {}
        def backtrack(i, holding):
            if i >= len(prices):
                return 0
            
            state = (i, holding)
            if state in memo:
                return memo[state]
            
            if holding:
                sell_now = prices[i] + backtrack(i+2, False)
                hold = backtrack(i+1, True)
                memo[state] = max(sell_now, hold)
                return memo[state]
            
            else:
                buy_now = -prices[i] + backtrack(i+1, True)
                wait = backtrack(i+1, False)
                memo[state]= max(buy_now, wait)
                return memo[state]
        result = backtrack(0, False)
       # print(memo)
        return result