class Solution:
    M = 1000000007
    
    def numDecodings(self, s: str) -> int:
        memo = [None]*len(s)
        return int(self.ways(s, len(s) - 1, memo))

    def ways(self, s, i, memo):
        if i < 0:
            return 1
        if memo[i] is not None:
            return memo[i]
        if s[i] == '*':
            res = 9 * self.ways(s, i - 1, memo) % self.M
            if i > 0 and s[i - 1] == '1':
                res = (res + 9 * self.ways(s, i - 2, memo)) % self.M
            elif i > 0 and s[i - 1] == '2':
                res = (res + 6 * self.ways(s, i - 2, memo)) % self.M
            elif i > 0 and s[i - 1] == '*':
                res = (res + 15 * self.ways(s, i - 2, memo)) % self.M
            memo[i] = res
            return memo[i]
        res = self.ways(s, i - 1, memo) if s[i] != '0' else 0
        if i > 0 and s[i - 1] == '1':
            res = (res + self.ways(s, i - 2, memo)) % self.M
        elif i > 0 and s[i - 1] == '2' and s[i] <= '6':
            res = (res + self.ways(s, i - 2, memo)) % self.M
        elif i > 0 and s[i - 1] == '*':
            res = (res + (2 if s[i] <= '6' else 1) * self.ways(s, i - 2, memo)) % self.M
        memo[i] = res
        return memo[i]
