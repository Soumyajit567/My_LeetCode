class Solution:
    def minElement(self, nums: List[int]) -> int:
        res = []
        for n in nums:
            pos_n = abs(n - 0)
            _sum = 0
            while n != 0:
                temp = n % 10
                _sum += temp
                n = n // 10
            if n < 0:
                _sum = 0 - _sum
                res.append(_sum)
            else:
                res.append(_sum)
        min_val =  min(res)
        return min_val

