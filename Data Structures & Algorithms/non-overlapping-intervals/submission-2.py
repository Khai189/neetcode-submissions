class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key = lambda x: x[0])
        print(intervals)
        prev_end = float("-inf")
        overlap = 0
        for i in range(len(intervals)):
            start, end = intervals[i]
            if prev_end <= start:
                prev_end = end
                continue
            
            else:
                overlap+=1
                prev_end = min(prev_end, end)
        
        return overlap