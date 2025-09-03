class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        res = float("infinity")
        minutes = []
        for time in timePoints:
            minut = int(time[0:2]) * 60
            minut+= int(time[3:])
            minutes.append(minut)
       
        minutes.sort()
        for i in range(1,len(minutes)):
            res = min(res,minutes[i]-minutes[i-1])
        circular_diff = 1440 - minutes[-1] + minutes[0]
        res = min(res,circular_diff)
        return res

            
