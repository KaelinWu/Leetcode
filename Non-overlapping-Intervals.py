class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])

        overlaps = 0
        print(intervals)
        prev = intervals[0][1]
        for i in range(1, len(intervals)):
            if prev > intervals[i][0]:
                overlaps+=1
            else:
                prev = intervals[i][1]
            
        return overlaps
