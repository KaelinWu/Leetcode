class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        n = len(words)

        res = 0
        def isprefix(str1,str2):
            m = len(str1)
            n = len(str2)
            return str2[:m] == str2[n-m:] == str1
        for i in range(n-1):
            for j in range(i+1,n):
                if isprefix(words[i],words[j]):
                    res+=1
        return res
