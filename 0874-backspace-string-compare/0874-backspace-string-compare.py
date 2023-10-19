class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # pointers for the current position in s and t
        i, j = len(s) - 1, len(t) - 1
        # counters for the number of skips (backspaces)
        skip_s, skip_t = 0, 0

        while i >= 0 or j >= 0:  # while there are chars to compare in either string
            while i >= 0:  # Find the next valid char in s
                if s[i] == '#':
                    skip_s += 1
                    i -= 1
                elif skip_s > 0:
                    skip_s -= 1
                    i -= 1
                else:
                    break  # found the current valid char in s

            while j >= 0:  # Find the next valid char in t
                if t[j] == '#':
                    skip_t += 1
                    j -= 1
                elif skip_t > 0:
                    skip_t -= 1
                    j -= 1
                else:
                    break  # found the current valid char in t

            # If the two actual characters are different
            if i >= 0 and j >= 0 and s[i] != t[j]:
                return False

            # If expecting to compare char vs nothing
            if (i >= 0) != (j >= 0):
                return False

            i -= 1
            j -= 1

        return True











"""
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
"""