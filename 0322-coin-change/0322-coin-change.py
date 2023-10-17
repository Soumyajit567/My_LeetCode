class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        n = len(coins)
        def memo(i):
            if i == 0:
                return 0
            elif i < 1:
                return -1
            elif i in dp:
                return dp[i]
            else:
                min_coins = float("inf")
                for coin in coins:
                    res = memo(i - coin)
                    if res >= 0:
                        min_coins = min(min_coins, res + 1)
            dp[i] = -1 if min_coins == float("inf") else min_coins
            return dp[i]

        return memo(amount)
        