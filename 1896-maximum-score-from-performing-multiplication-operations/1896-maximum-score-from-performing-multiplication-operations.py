"""
class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        dp = {}
        m = len(nums)
        n = len(multipliers)
        @cache
        def memo(i, j):
            right = len(nums) - (j - i) - 1
            if j == n:
                return 0
            elif (i, j) in dp:
                return dp[(i, j)]
            else:
                dp[(i, j)] = max(nums[i] * multipliers[j] + memo(i + 1, j + 1), nums[right] * multipliers[j] + memo(i, j + 1))
                return dp[(i, j)]

        return memo(0, 0)
"""

class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:

        # Number of Operations
        m = len(multipliers)

        # For Right Pointer
        n = len(nums)

        dp = [[0] * (m + 1) for _ in range(m + 1)]

        for op in range(m - 1, -1, -1):
            for left in range(op, -1, -1):

                dp[op][left] = max(multipliers[op] * nums[left] + dp[op + 1][left + 1],
                                   multipliers[op] * nums[n - 1 - (op - left)] + dp[op + 1][left])

        return dp[0][0]
 