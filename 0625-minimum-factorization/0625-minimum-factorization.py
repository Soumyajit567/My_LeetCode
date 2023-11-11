class Solution:
    def smallestFactorization(self, num: int) -> int:
        if num < 2:
            return num
        factors = []
        for i in range(9, 1, -1):
            while num % i == 0:
                factors.append(i)
                num //= i
        if num > 1:
            return 0
        result = int(''.join(map(str, reversed(factors))))
        return result if result < 2**31 else 0