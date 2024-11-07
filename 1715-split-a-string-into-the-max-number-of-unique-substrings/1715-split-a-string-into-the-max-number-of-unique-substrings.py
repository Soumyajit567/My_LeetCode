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
                        unique_substrings.add(sub)
                        stack.append((end, unique_substrings.copy()))
                        unique_substrings.remove(sub)
        return max_len
