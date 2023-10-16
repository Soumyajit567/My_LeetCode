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