class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def dfs(opened,closed,path):
            if opened == closed == n:
                res.append(path)
                return
            if opened<n:
                dfs(opened+1,closed,path+\(\)
            if closed < opened:
                dfs(opened,closed+1,path+\)\)
                
            

            
        dfs(0,0,\\)
        return res

#def dfs(close, opened, path, curr):
            
        #     if close > opened:
        #         return
        #     if close == opened == n:
        #         res.append(path)
        #         return
        #     for i in range(curr,2*n):
        #         dfs(close, opened+1, path + \(\, i+1)
        #         dfs(close + 1, opened, path + \)\, i+1)