class Solution:
    def minSteps(self, n: int) -> int:
        # If n is 1, then we already have the character 'A' on the screen.
        if n == 1:
            return 0

        # The dp array where dp[i] will store the minimum number of operations to get 'i' 'A's.
        dp = [0] * (n + 1)

        for i in range(2, n + 1):
            # Initially set the current state to a large number.
            dp[i] = float('inf')
            for j in range(1, i):
                # If the current number of 'A's is divisible by 'j', then it means we can obtain 'i' by
                # copying the 'j' 'A's (1 operation) and pasting it (i/j - 1) times.
                if i % j == 0:
                    dp[i] = min(dp[i], dp[j] + (i // j))

        return dp[n]