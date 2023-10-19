class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack = []
        stack2 = []
        i = 0
        j = 0
        while i < len(s):
            if s[i] == "#":
                if stack:
                    stack.pop()

            elif s[i] != "#":
                stack.append(s[i])
            i += 1

        while j < len(t):
            if t[j] == "#":
                if stack2:
                    stack2.pop()
            elif t[j] != "#":
                stack2.append(t[j])
            j += 1
        return "".join(stack) == "".join(stack2)
