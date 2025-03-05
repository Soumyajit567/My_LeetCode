class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        p = set()
        limit = math.floor(math.log10(10**7) / math.log10(3))
        def backtrack(i, _sum, p):
            if _sum == n:
                return True
            if _sum > n:
                return False
            
            for k in range(i, limit + 1):  
                if k not in p:
                    p.add(k)
                    if backtrack(k + 1, _sum + pow(3, k), p):
                        return True
                    p.remove(k)
            return False
        
        return backtrack(0, 0, p)