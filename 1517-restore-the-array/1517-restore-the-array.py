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