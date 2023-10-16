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
        # Number of operations to be performed
        m = len(multipliers)
        # Length of the nums list
        n = len(nums)

        # Initialize a 2D dp array with dimensions (m+1) x (m+1)
        dp = [[0] * (m + 1) for _ in range(m + 1)]

        # We start from the last operation and move to the first one
        for op in range(m - 1, -1, -1):
            # The 'left' index can go from 'op' to 0
            for left in range(op, -1, -1):
                # Calculate the 'right' index for taking an element from the end of 'nums'
                # It's determined by how many elements are already taken from the start ('left')
                # and how many operations have been performed ('op')
                right = n - 1 - (op - left)  # Calculate the corresponding right index

                # Update the dp table considering two choices: 
                # taking the next element either from the start or the end of the 'nums' list
                # The current operation 'op' is used to pick the multiplier, and the 'left' index
                # is used to pick an element from the start of the 'nums' list.
                dp[op][left] = max(
                    multipliers[op] * nums[left] + dp[op + 1][left + 1],  # Choose from the start
                    multipliers[op] * nums[right] + dp[op + 1][left]  # Choose from the end
                )

        # The answer is in dp[0][0] which considers all operations starting from 0
        return dp[0][0]
