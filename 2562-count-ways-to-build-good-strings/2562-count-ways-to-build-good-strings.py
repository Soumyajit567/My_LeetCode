class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = {}
        mod = 10 ** 9 + 7
        def memo(i):
            if i > high:
                return 0
            elif i in dp:
                return dp[i] 
            elif i >= low:               
                dp[i] = 1 
            else:
                dp[i] = 0
            dp[i] += memo(i + zero) + memo(i + one)
            return dp[i] % mod


        return memo(0)



