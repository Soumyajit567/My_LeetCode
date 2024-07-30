class Solution:
    def checkString(self, s: str) -> bool:
        if 'a' not in s or 'b' not in s:
            return True
        for i in range(1, len(s)):
            if s[i-1] == 'b' and s[i] == 'a':
                return False
        
        return True