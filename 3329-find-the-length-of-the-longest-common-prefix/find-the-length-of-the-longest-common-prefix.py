class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefix = set()

        for num in arr1:
            while num  != 0:
                
                prefix.add(num)
                num //= 10
        
        res = 0
        pre = 0
        for num in arr2:
            while num != 0:
                
                if num in prefix:
                    res = max(len(str(num)),res)
                    pre = max(pre,num)
                    break
                num //= 10
        return res

