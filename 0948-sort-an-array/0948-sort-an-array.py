import heapq
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        minHeap = [i for i in nums]
        res = []
        heapq.heapify(minHeap)
        while minHeap:
            val = heapq.heappop(minHeap)
            res.append(val)
        return res