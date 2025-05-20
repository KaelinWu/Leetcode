class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        bfs = deque()
        fresh =0
        for row in range(ROW):
            for col in range(COL):
                if grid[row][col] == 1:
                    fresh+=1
                elif grid[row][col] == 2:
                    bfs.append((row,col))

        directions = [[0,1], [0,-1], [-1,0], [1,0]]
        time = 0
        while bfs and fresh:
            length = len(bfs)
            for i in range(length):
                r,c = bfs.popleft()
                for dr, dc in directions:
                    row = r+dr
                    col = c+dc
                    if row in range(ROW) and col in range(COL) and grid[row][col] ==1:
                        fresh-=1
                        grid[row][col] =2
                        bfs.append((row,col))
            time+=1
        
        if fresh == 0:
            return time
        return -1


        
