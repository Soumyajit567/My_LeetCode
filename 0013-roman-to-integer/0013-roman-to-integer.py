class Solution:
    def romanToInt(self, s: str) -> int:
        summ = 0
        hasmap ={'I':1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}

        for i in range(len(s)):
            if i+1 < len(s) and hasmap[s[i]] < hasmap[s[i+1]]:
                summ-=hasmap[s[i]]
            else:
                summ+=hasmap[s[i]]
        return summ
            