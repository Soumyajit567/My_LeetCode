class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = []
        res.append(0)
        for i in range(n):
            prev_len = len(res)
            prev = i
            mask = 1 << prev
            for j in range(prev_len - 1, -1, -1):
                res.append((mask | res[j]))
        return res