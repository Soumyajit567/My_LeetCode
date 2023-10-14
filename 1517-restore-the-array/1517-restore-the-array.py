class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        MOD = 10**9 + 7
        n = len(s)
        dp = [0] * (n + 1)  # dp[i] is the number of ways to print valid arrays from substring s[i:]
        dp[n] = 1  # base case
        
        for i in range(n - 1, -1, -1):  # start from the end of the string
            if s[i] == '0':  # numbers in the array can't start with a zero
                continue
            num = 0
            for j in range(i, n):
                num = num * 10 + int(s[j])  # building the number
                if num > k:
                    break  # if we exceed k, no need to go further
                dp[i] = (dp[i] + dp[j + 1]) % MOD  # this substring is valid, add the number of ways from the rest of the string
        
        return dp[0]  # the result is the number of ways to print the array from the start of the string

"""
Initialization:

dp = [0, 0, 0, 0, 1] (n = 4, length of "1317", and dp[n] = 1)
Start of outer loop:

Outer loop i goes from 3 to 0
i = 3 ("7"):

Inner loop j goes from 4 to 3
num = 7, num <= k, dp[3] += dp[4]
dp[3] = 0 + 1 = 1 after all inner loop iterations
dp = [0, 0, 0, 1, 1]
i = 2 ("1"):

Inner loop j goes from 4 to 2
num = 1, num <= k, dp[2] += dp[4]
num = 17, num <= k, dp[2] += dp[3]
dp[2] = 0 + 1 + 1 = 2 after all inner loop iterations
dp = [0, 0, 2, 1, 1]
i = 1 ("3"):

Inner loop j goes from 4 to 1
num = 3, num <= k, dp[1] += dp[4]
num = 31, num <= k, dp[1] += dp[3]
num = 317, num <= k, dp[1] += dp[2]
dp[1] = 0 + 1 + 1 + 2 = 4 after all inner loop iterations
dp = [0, 4, 2, 1, 1]
i = 0 ("1"):

Inner loop j goes from 4 to 0
num = 1, num <= k, dp[0] += dp[4]
num = 13, num <= k, dp[0] += dp[3]
num = 131, num <= k, dp[0] += dp[2]
num = 1317, num <= k, dp[0] += dp[1]
dp[0] = 0 + 1 + 1 + 2 + 4 = 8 after all inner loop iterations
dp = [8, 4, 2, 1, 1]
End of outer loop.

Final dp array: [8, 4, 2, 1, 1]

The result is dp[0] = 8.
This represents the total number of ways you can partition the string "1317" into sub-strings that are valid integers and do not exceed 2000. Each iteration of the inner loop essentially considers a different partitioning of the string, and the dp array accumulates the count of valid partitions.

"""