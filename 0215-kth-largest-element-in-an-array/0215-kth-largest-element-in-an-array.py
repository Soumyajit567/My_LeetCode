class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-n for n in nums]
        heapq.heapify(heap)
        while heap and k - 1 >= 0:
            val = -heapq.heappop(heap)
            k -= 1
        return val

