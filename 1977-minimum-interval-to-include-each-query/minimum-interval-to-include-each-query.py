class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        print(intervals)
        minheap = []
        res = {}
        i = 0
        for que in sorted(queries):
            while i < len(intervals) and que >= intervals[i][0]:
                l,r = intervals[i]
                heapq.heappush(minheap,(r-l+1,r))
                i+=1
            
            while minheap and que > minheap[0][1]:
                heapq.heappop(minheap)
            if minheap:
                res[que] = minheap[0][0]
            else:
                res[que] = -1
        return [res[que] for que in queries]