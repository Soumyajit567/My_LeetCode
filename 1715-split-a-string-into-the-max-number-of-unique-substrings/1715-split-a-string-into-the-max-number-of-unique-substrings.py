# Backtracking like stack to save time

class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        max_unique_count = 0
        n = len(s)
        
        # Stack holds tuples of (current index, set of unique substrings, path)
        stack = [(0, set())]  # We include an empty list to track each path for demonstration

        while stack:
            start, unique_substrings = stack.pop()
            
            # If we reach the end of the string, update the maximum count
            if start == n:
                max_unique_count = max(max_unique_count, len(unique_substrings))
                #print(f"Valid split path: {path} -> Unique count: {len(unique_substrings)}")
                continue

            # Try each substring starting from the current index
            for end in range(start + 1, n + 1):
                substring = s[start:end]
                
                if substring not in unique_substrings:
                    # In-place add and manually create new path state
                    unique_substrings.add(substring)
                    # new_path = path + [substring]
                    
                    # Push new state to stack (like recursive call)
                    stack.append((end, unique_substrings.copy()))
                    
                    # In-place backtracking (remove to reset for the next iteration)
                    unique_substrings.remove(substring)

        return max_unique_count