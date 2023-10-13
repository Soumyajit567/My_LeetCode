class Solution:
    def maxA(self, n: int) -> int:
        dp = [0] * (n + 1)
    
        for i in range(1, n + 1):
            # Pressing 'A'
            dp[i] = dp[i - 1] + 1
            for j in range(2, i):
                # Ctrl-A, Ctrl-C, then Ctrl-V several times
                dp[i] = max(dp[i], dp[j - 2] * (i - j + 1))

        return dp[n]

"""
class Solution:
    def maxA(self, n: int) -> int:
        dp = list(range(n + 1))
        for i in range(n - 2):
            for j in range(i + 3, min(n, i + 6) + 1):
                dp[j] = max(dp[j], (j - i - 1) * dp[i])
        return dp[n]
"""