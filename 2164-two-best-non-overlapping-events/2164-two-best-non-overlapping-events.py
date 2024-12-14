class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort(key = lambda x: x[0])
        heap = []
        max_single_event = 0
        max_score = 0
        for start, end, value in events:
            while heap and heap[0][0] < start:
                prev_end , prev_value = heapq.heappop(heap)
                max_single_event = max(max_single_event, prev_value)
            max_score = max(max_score, max_single_event + value)
            heapq.heappush(heap,(end, value))
        return max_score