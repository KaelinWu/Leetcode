class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []
        for i in range(n-2,-1,-1):
            j = i+1
            while temperatures[i] >= temperatures[j]:
                if res[j] == 0:
                    j = n
                    break
                j += res[j]
            
            if j < n:
                res[i] = j-i

        return res


        

        return res
