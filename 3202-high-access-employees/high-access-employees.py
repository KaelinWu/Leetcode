class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        access_times.sort(key = lambda x: (x[0], x[1]))

        def convert(time):
            hour = int(time[:2])
            minute = int(time[2:])
            return hour * 60 + minute
        
        i = 0
        res = []
        n = len(access_times)
        while i < n:
            employee, strtime = access_times[i]
            
            j = i
            count = 0
            times = []
            while j < n and access_times[j][0] == employee:
                times.append(convert(access_times[j][1]))
                j+=1
            left = 0
            for right in range(len(times)):
                while times[right] - times[left] >= 60:
                    left+=1
                if right-left+1 >= 3:
                    res.append(employee)
                    break
            i = j

        return res