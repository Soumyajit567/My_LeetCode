from itertools import permutations
class Solution:
    def stringCount(self, n: int) -> int:
        dp = {}
        mod = 10**9 + 7
        T = (1 << 4) - 1    
            
        def solve(idx, v): 
            if idx == n and v == T:
                return 1 
            if idx == n: 
                return 0
            
            if (idx, v) in dp: 
                return dp[(idx, v)]
        
            ans = 0 
            ans += 23 * solve(idx + 1, v)
            ans += solve(idx + 1, v | (1 << 0))
            ans += solve(idx + 1, v | (1 << 1))
            
            if (v >> 2) & 1: 
                ans += solve(idx + 1, v | (1 << 3))
            else:
                ans += solve(idx + 1, v | (1 << 2))
            
            ans %= mod
            dp[(idx, v)] = ans
            return ans
        
        return solve(0, 0)  