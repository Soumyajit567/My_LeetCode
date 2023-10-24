class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        max_so_far = -1
        chunks = 0
        for i, num in enumerate(arr):
            max_so_far = max(max_so_far, num)
            if max_so_far == i:
                chunks += 1
        return chunks



"""
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        
        left_max = [0] * n
        right_min = [float('inf')] * n
        
        # Populating left_max
        left_max[0] = arr[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i-1], arr[i])
        
        # Populating right_min
        right_min[-1] = arr[-1]
        for i in range(n-2, -1, -1):
            right_min[i] = min(right_min[i+1], arr[i])
        
        # Calculating chunks
        chunks = 1  # At least one chunk: the whole array
        for i in range(n-1):
            if left_max[i] <= right_min[i+1]:
                chunks += 1
        
        return chunks
"""