class Solution:
    def checkString(self, s: str) -> bool:
        count = Counter(s)
        boolean = True
        if "a" not in count or "b" not in count:
                boolean = True
        for ch in range(1, len(s)):
            if s[ch - 1] == "b" and s[ch] == "a":
                boolean = False
        return True if boolean else False