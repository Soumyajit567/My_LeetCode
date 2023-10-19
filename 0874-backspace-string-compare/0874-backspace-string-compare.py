class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def next_char(string, index):
            backspace_count = 0
            while index >= 0:
                if string[index] == '#':  # it's a backspace character
                    backspace_count += 1
                elif backspace_count > 0:  # it's a character to be deleted
                    backspace_count -= 1
                else:
                    break  # it's a valid character
                index -= 1  # move to the previous character
            return index

        i, j = len(s) - 1, len(t) - 1
        while i >= 0 or j >= 0:
            i, j = next_char(s, i), next_char(t, j)  # find the next valid character or -1 if none
            if i < 0 and j < 0:  # reached the start of both strings
                return True
            if i < 0 or j < 0:  # reached the start of only one string
                return False
            if s[i] != t[j]:  # the characters do not match
                return False

            # move to the previous character
            i -= 1
            j -= 1

        return True  # all valid characters matched