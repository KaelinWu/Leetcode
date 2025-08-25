class Solution:
    def minTime(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        if n == 1:
            return 0
        if edges == []:
            return -1
        for src, dst, start, end in edges:
            adj[src].append((start,end,dst))

        heap = []
        
        heap.append((0,0))
        visited = set()
        while heap:
            time, curr = heapq.heappop(heap)
            if curr in visited:
                continue
            
            if curr == n-1:
                return time 
            visited.add(curr)
            for start,end,dst in adj[curr]:
                if end < time or dst in visited:
                    continue
                if start >= time:
                    heapq.heappush(heap,(start+1,dst))
                else:
                    heapq.heappush(heap,(time+1,dst))
                
        return -1