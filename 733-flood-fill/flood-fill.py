class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        directions = [[0,1], [1,0], [-1,0], [0,-1]]
        ROW,COL = len(image),len(image[0])
        
        org = image[sr][sc]
        def dfs(row,col):
            if row < 0 or col < 0 or row >= ROW or col >= COL or image[row][col] != org or image[row][col] == color:
                return
            #print(org)
            # if image[row][col] != org or image[row][col] == color:
            #     return
            image[row][col] = color
            for dr,dc in directions:
                dfs(row+dr,col+dc)
            return
        dfs(sr,sc)
        return image
