class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], x[1]))  
        count = 0  
        last_included_end = intervals[0][1]  

        for interval in intervals[1:]:
            if interval[0] < last_included_end:
                count += 1  
                last_included_end = min(last_included_end, interval[1])  
            else:
                last_included_end = interval[1]  

        return count
            