class Solution:
    def findPermutation(self, s: str) -> List[int]:
        n = 1
        res = [n]

        for i, p in enumerate(s):
            if p == "I":
                res.append(n+1)
                n += 1
            elif p == "D":
                ins = i
                while ins >= 0 and s[ins] == "D":
                    ins -= 1
                res.insert(ins+1, n+1)
                n += 1
        
        return res