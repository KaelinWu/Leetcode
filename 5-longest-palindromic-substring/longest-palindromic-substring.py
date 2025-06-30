class Solution:
    def longestPalindrome(self, s: str) -> str:
        def manachers(string):
            t = "#" + "#".join(string) + "#"
            n = len(t)
            p = [0] * n
            l,r = 0,0
            for i in range(n):
                p[i] = min(r - i, p[l + (r - i)]) if i < r else 0
                while i-p[i]-1 >= 0 and i+p[i]+1 < n and t[i+p[i]+1] == t[i-p[i]-1]:
                    p[i]+=1
                if i + p[i] > r:
                    r = i+p[i]
                    l = i-p[i]
            return p
        p = manachers(s)
        print(p)
        reslen,index = max((v,i) for i,v in enumerate(p))
        start = (index-reslen)//2
        return s[start:start + reslen]