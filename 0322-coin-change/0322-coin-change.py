class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        n = len(coins)
        def memo(i):
            if i == amount:
                return 0
            elif i > amount:
                return -1 
            elif i in dp:
                return dp[i]
            else:
                min_count = float("inf")
                for coin in coins:
                    count = memo(i + coin)
                    if count >= 0:
                        min_count = min(min_count, count + 1)
                dp[i] = -1 if min_count == float("inf") else min_count
                return dp[i]

        return memo(0)