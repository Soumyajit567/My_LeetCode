class Solution:
    def splitLoopedString(self, strs: List[str]) -> str:
        strs = [max(x, x[::-1]) for x in strs]        
        ans = ""
        for i in range(len(strs)): 
            rev = strs[i][::-1]
            rest = "".join(strs[i+1:] + strs[:i])
            for k in range(len(strs[i])): 
                ans = max(ans, strs[i][k:] + rest + strs[i][:k])
                ans = max(ans, rev[k:] + rest + rev[:k])
        return ans 