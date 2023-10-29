class Solution:
    def countVowelPermutation(self, n: int) -> int:
        mod = 10**9 + 7
        
        # Transition matrix based on the given rules
        transitions = [
            [0, 1, 0, 0, 0],  # from 'a'
            [1, 0, 1, 0, 0],  # from 'e'
            [1, 1, 0, 1, 1],  # from 'i'
            [0, 0, 1, 0, 1],  # from 'o'
            [1, 0, 0, 0, 0]   # from 'u'
        ]
        
        # Initialization: For n = 1, there are 5 possibilities
        dp = [1, 1, 1, 1, 1]
        
        for i in range(2, n + 1):
            new_dp = [0, 0, 0, 0, 0]
            for j in range(5):
                for k in range(5):
                    if transitions[j][k]:
                        new_dp[k] = (new_dp[k] + dp[j]) % mod
            dp = new_dp
        
        return sum(dp) % mod





"""
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        dp = {}
        mod = 10 ** 9 + 7
        string = ""
        
        @cache
        def memo(i, s):
            nonlocal mod
            
            if i == n:
                return 1
            
            if (i, s) in dp:
                return dp[(i, s)]
            
            count = 0
            for ch in "aeiou":
                if s == "":
                    count += memo(i + 1, ch)
                    continue
                else:
                    if s[-1] == "a" and ch != "e":
                        continue
                    elif s[-1] == "e" and (ch != "a" and ch != "i"):
                        continue
                    elif s[-1] == "i" and ch == "i":
                        continue
                    elif s[-1] == "o" and (ch != "i" and ch != "u"):
                        continue
                    elif s[-1] == "u" and ch != "a":
                        continue

                count += memo(i + 1, s + ch)
            dp[(i, s)] = count % mod
            return count % mod
                    
        return memo(0, string) % mod
"""