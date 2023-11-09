class Solution:
    def countHomogenous(self, s: str) -> int:
        count = 1
        ans = 1
        for ch in range(1, len(s)):
            if s[ch] == s[ch - 1]:
                count += 1
            else:
                count = 1
            ans = (ans + count) % (10**9 + 7)
        return ans
            