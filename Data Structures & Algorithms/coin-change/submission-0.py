class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        # index i into table `a` stores the minimum number of coins
        # to make up amount i
        smallest_coin = coins[0]
        # impossible to make any amount smaller than the smallest coin
        a = [0]
        for i in range(1, amount + 1):
            min_coin_count = float('inf')
            for c in coins:
                if i - c >= 0 and a[i-c] >= 0:
                    min_coin_count = min(min_coin_count, 1 + a[i - c])
            if min_coin_count == float('inf'):
                a.append(-1)
            else:
                a.append(min_coin_count)
        return a[amount]
 




