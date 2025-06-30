class Solution:
    def countSubstrings(self, s: str) -> int:
        def manachers(string):
            t = "#" + "#".join(string) + "#"
            n = len(t)
            p = [0] * n
            l,r = 0,0
            for i in range(n):
                p[i] = min(r-i,p[l+r-i]) if r >i else 0
                while i+p[i] + 1 < n and i-p[i]-1 >=0 and t[i+p[i] + 1] == t[i-p[i]-1]:
                    p[i]+=1
                if i+p[i] > r:
                    r = i+p[i]
                    l = i-p[i]
            return p
        res = 0
        p = manachers(s)
        for val in p:
            res += (val+1) // 2
        return res