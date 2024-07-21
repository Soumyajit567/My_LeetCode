class Solution:
    def maxOperations(self, s: str) -> int:
        tmp = []
        for c in s:
            if tmp and tmp[-1] == '0' and c == '0':
                continue
            else:
                tmp.append(c)
        ans = 0
        cnt = 0
        for c in tmp:
            if c == '0':
                ans += cnt
            else:
                cnt += 1
        return ans