class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}  
        @cache
        def memo(i):

            if i == amount:
                return 0
            if i > amount:
                return -1
            
         
            if i in dp:
                return dp[i]

            min_count = float("inf")  
            
            for coin in coins:
                res = memo(i + coin)  
                if res >= 0: 
                    min_count = min(min_count, res + 1)  

            dp[i] = -1 if min_count == float("inf") else min_count
            return dp[i]

        return memo(0) 