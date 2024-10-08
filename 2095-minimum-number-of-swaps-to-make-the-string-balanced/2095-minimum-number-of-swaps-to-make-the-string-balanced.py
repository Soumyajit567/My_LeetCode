class Solution:
    def minSwaps(self, s: str) -> int:
        count = 0
        max_count = 0
        for ch in s:
            if ch == "[":
                count -= 1
            else:
                count += 1
            max_count = max(max_count, count)
        return (max_count + 1)//2


