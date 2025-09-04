class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        c = Counter(nums)
        res = 0

        for num in c:
            if k == 0:

                if c[num] > 1:
                    res +=1
            else:
                if num + k in c:
                    res+=1
        return res