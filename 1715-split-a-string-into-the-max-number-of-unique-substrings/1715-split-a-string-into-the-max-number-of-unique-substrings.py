class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        max_unique_count = 0
        n = len(s)
        stack = [(0, set())]  

        while stack:
            start, unique_substrings = stack.pop()
            
            if start == n:
                max_unique_count = max(max_unique_count, len(unique_substrings))
                continue

            for end in range(start + 1, n + 1):
                substring = s[start:end]
                if substring not in unique_substrings:
                    new_unique_substrings = unique_substrings | {substring}
                    stack.append((end, new_unique_substrings))
        
        return max_unique_count