# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         memo = {}

#         def helper(start: int, end: int) -> str:
#             if (start, end) in memo:
#                 return memo[(start, end)]

           
#             if end - start < 2:
#                 return s[start:end]

#             if s[start] == s[end - 1] and helper(start + 1, end - 1) == s[start + 1:end - 1]:
#                 result = s[start:end]
#             else:
#                 result = max(helper(start + 1, end), helper(start, end - 1), key=len)

#             memo[(start, end)] = result

#             return result

#         return helper(0, len(s))
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[0] * (len(s)) for _ in range(len(s))]
        ans = ""
        max_len = 0
        for length in range(len(s)):
            for i in range(len(s)):
                j = i + length
                if j >= len(s):
                    break
                if length == 0:
                    dp[i][j] = 1
                elif length == 1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = dp[i + 1][j - 1] and (s[i] == s[j])
                if dp[i][j] and length + 1 > max_len:
                    max_len = length + 1
                    ans = s[i : j + 1]
        return ans                   
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        reslen = 0
        for i in range(len(s)):
                l, r = i, i
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    if (r - l + 1) > reslen:
                        reslen = r - l + 1
                        res = s[l : r + 1]
                    l -= 1
                    r += 1
                l, r = i, i + 1
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    if (r - l + 1) > reslen:
                        reslen = r - l + 1
                        res = s[l : r + 1]

                    l -= 1
                    r += 1
        return res   

