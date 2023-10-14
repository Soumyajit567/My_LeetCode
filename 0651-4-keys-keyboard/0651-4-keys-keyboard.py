class Solution:
    def maxA(self, n: int) -> int:
        @functools.cache
        def dp(i):
            if i <= 0:
                return 0
            max_count = dp(i - 1) + 1  # pressing 'A'
            for j in range(1, i - 2):  # leave at least two steps for Ctrl-A and Ctrl-C, and one for Ctrl-V
                # It's i - j - 1 because we're using i - j steps after j, and one of them is used for Ctrl-V.
                max_count = max(max_count, dp(j) * (i - j - 1))  # Ctrl-A, Ctrl-C, followed by (i - j - 1) times Ctrl-V
            return max_count

        return dp(n)




"""
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

"""
class Solution:
    def maxA(self, n: int) -> int:
        dp = list(range(n + 1))
        for i in range(n - 2):
            for j in range(i + 3, min(n, i + 6) + 1):
                dp[j] = max(dp[j], (j - i - 1) * dp[i])
        return dp[n]
"""