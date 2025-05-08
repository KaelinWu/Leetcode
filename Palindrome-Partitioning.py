class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        print(s[0:1])
        def is_pali(word):
            return word == word[::-1]
        
        def backtracking(start, subset):
            if start == len(s):
                res.append(subset[:])
                return
            
            for i in range(start, len(s)):
                string = s[start:i+1]
                if is_pali(string):
                    backtracking(i+1, subset + [string])

        backtracking(0,[])
        return res
                    
                

