class Solution:
    def numSub(self, s: str) -> int:
        count = 0
        ans = 0
        for i in range(len(s)):
            if s[i] == "1" and s[i] == s[i - 1]:
                count += 1
            elif s[i] == "1":
                count = 1
            elif s[i] == "0":
                count = 0
            ans = (ans + count) % (10**9 + 7)
        return ans
