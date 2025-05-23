class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        ROW = len(heights)
        COL = len(heights[0])
        alt, pac = set(), set()
        directions = [[1,0], [-1,0], [0,-1], [0,1]]
        def dfs(row,col,visited,previous):
            if (row,col) in visited or row < 0 or col< 0 or row >=ROW or col >= COL or heights[row][col] < previous:
                return
            visited.add((row,col))
            for dr, dc in directions:
                dfs(dr+row,dc+col,visited,heights[row][col])
        for row in range(ROW):
            dfs(row,0,pac,0)
            dfs(row,COL-1,alt,0)
        
        for col in range(COL):
            dfs(0,col,pac,0)
            dfs(ROW-1,col,alt,0)
        for row in range(ROW):
            for col in range(COL):
                if (row,col) in alt and (row,col) in pac:
                    res.append((row,col))
        return res

            

            

                