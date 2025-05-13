class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        directions = [[0,1], [0,-1], [-1,0], [1,0]]
        ROW = len(grid)
        COL = len(grid[0])
        visit = set()
        def dfs(row, col):
            if row < 0 or col < 0 or row >= ROW or col >= COL or (row,col) in visit or grid[row][col] == 0:
                return 0
            visit.add((row,col))
            area = 1 + dfs(row-1, col) + dfs(row+1,col) + dfs(row, col-1) + dfs(row, col+1)
            
            return area
    
        for row in range(ROW):
            for col in range(COL):
                
                max_area = max(dfs(row,col), max_area)
        return max_area
            







        return max_area