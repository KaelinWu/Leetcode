class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort()
        slots2.sort()

        one = 0
        two = 0

        while one < len(slots1) and two < len(slots2):
            
            u1,u2 = slots1[one]
            v1,v2 = slots2[two]
            high = 0
            low = 0
            if v2 > u2:
                high = u2
            else:
                high = v2
            
            if u1 > v1:
                low = u1
            else:
                low = v1
            interval = min(v2,u2) - max(u1,v1)

            if interval >= duration:
                return [low,low+duration]
            if v2 < u2:
                two+=1
            else:
                one+=1
        return []