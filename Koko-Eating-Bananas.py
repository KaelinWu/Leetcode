class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = max(piles)

        r= res
        l = 1
        
        while l <= r:
            pivot = (r+l)//2
            
            time = 0
            for p in piles:
                time += math.ceil(float(p)/pivot)
            if time <= h:
                r = pivot-1
                res = pivot
            else:
                l = pivot+1
                

            
        return res
