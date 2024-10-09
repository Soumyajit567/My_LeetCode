class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        left = 0
        right = 0
        stack = []
        for i, ch in enumerate(s):
            if ch == "(":
                stack.append(i)
                left += 1
            elif ch == ")":
                if stack:
                    stack.pop()
                    left -= 1
                else:
                    right += 1
        return left + right

