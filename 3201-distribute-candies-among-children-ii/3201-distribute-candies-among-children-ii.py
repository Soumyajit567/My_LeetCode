class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        ans = 0
        for i in range(limit+1):
            j = n - i
            if j < 0:
                break
            else:
                mul = limit * 2
                if mul >= j:
                    if j > limit:
                        j -= limit
                        ans += limit - j + 1
                    else:
                        ans += (j+1)
        return ans