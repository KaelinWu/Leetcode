class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort()
        slots2.sort()

        i1 = 0
        i2 = 0
        n,m = len(slots1), len(slots2)
        while i1 < n and i2 < m:
            u1,u2 = slots1[i1]
            v1,v2 = slots2[i2]
            
            low = max(slots2[i2][0],slots1[i1][0])
            interval = min(slots2[i2][1],slots1[i1][1]) - low

            if interval >= duration:
                return [low, low+duration]
            
            if u2 > v2:
                i2+=1
            else:
                i1+=1

        return []

        return []