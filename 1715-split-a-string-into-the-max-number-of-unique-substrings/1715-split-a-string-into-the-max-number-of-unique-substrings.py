class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        n = len(s)
        max_len = 0
        unique = set()
        stack = [(0, set())]
        while stack:
            start, unique_substrings = stack.pop()
            if start == n:
                max_len = max(max_len, len(unique_substrings))
                continue
            else:
                for end in range(start + 1, n + 1):
                    sub = s[start:end]
                    if sub not in unique_substrings:
                        new_unique_substrings = unique_substrings | {sub}
                        stack.append((end, new_unique_substrings))
        return max_len
