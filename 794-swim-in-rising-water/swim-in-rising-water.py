class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        minheap = [(grid[0][0],0,0)]
        visited = set((0,0))
        while minheap:
            time,row,col = heapq.heappop(minheap)
            if (row,col) == (n-1,n-1):
                return time
            for dr,dc in directions:
                r,c = row+dr,col+dc
                if r < 0 or c < 0 or r >= n or c >= n or (r,c) in visited:
                    continue
                newtime = grid[r][c]
                visited.add((r,c))

                heapq.heappush(minheap,(max(time,newtime),r,c))
        
            
        

        