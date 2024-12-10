class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        # Sort events by start time
        events.sort(key=lambda x: x[0])
        
        max_score = 0
        max_single_event = 0
        heap = []  # Min-heap to store events based on their end time
        
        for start, end, value in events:
            # Remove all events from the heap that end before the current event starts
            while heap and heap[0][0] < start:
                prev_end, prev_value = heapq.heappop(heap)
                # Update the max single event value with the best event seen so far
                max_single_event = max(max_single_event, prev_value)
            
            # Update the max score considering the current event and the best previous event
            max_score = max(max_score, max_single_event + value)
            
            # Push the current event into the heap
            heapq.heappush(heap, (end, value))
        
        return max_score