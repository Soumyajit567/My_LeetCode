class Solution:
    @functools.cache
    def maxA(self, n: int) -> int:
        if n <= 5:
            return n
        else:
            return max(n, max(i * self.maxA(n - i - 1) for i in [3, 4, 5, 6]))

"""
class Solution:
    def maxA(self, n: int) -> int:
        dp = list(range(n + 1))
        for i in range(n - 2):
            for j in range(i + 3, min(n, i + 6) + 1):
                dp[j] = max(dp[j], (j - i - 1) * dp[i])
        return dp[n]
"""