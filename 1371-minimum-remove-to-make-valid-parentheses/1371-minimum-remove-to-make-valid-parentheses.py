class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        popper = set()
        for ch in range(len(s)):
            if s[ch] == "(":
                stack.append(ch)
            elif s[ch] == ")":
                stack.pop() if stack else popper.add(ch)
        popper = popper.union(set(stack))
        res = "".join([ch for idx, ch in enumerate(s) if idx not in popper])
        return res
            