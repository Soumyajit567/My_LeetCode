class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        # Sort events by end time
        events.sort(key=lambda x: x[1])
        
        # Store the maximum value up to each event
        max_val = [0] * len(events)
        max_so_far = 0
        
        for i in range(len(events)):
            max_so_far = max(max_so_far, events[i][2])
            max_val[i] = max_so_far
        
        # Extract end times for binary search
        end_times = [event[1] for event in events]
        
        max_score = 0

        for i in range(len(events)):
            # Find the latest event that ends before the current event starts
            idx = bisect_right(end_times, events[i][0] - 1) - 1
            if idx >= 0:
                max_score = max(max_score, events[i][2] + max_val[idx])
            else:
                max_score = max(max_score, events[i][2])

        return max_score