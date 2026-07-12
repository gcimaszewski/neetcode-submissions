class Solution:
    """
    Coin Change II

    """
    def change(self, amount: int, coins: List[int]) -> int:
        # let dp[i] = number of ways to make i with coins
        # for coins a, b, c:
        # dp[i] = dp[i-a] + dp[i-b] + dp[i-c]
        coins.sort()
      #  dp = [[0]*(amount+1) for _ in range(len(coins))]
        dp = [0 for _ in range(amount + 1)]
        dp[0] = 1 # only one way to have $0: no coins
        for c in coins:
            for i in range(c, amount+1):
                if c > i:
                    break
                dp[i] += dp[i-c]
        print(dp)
        return dp[amount]