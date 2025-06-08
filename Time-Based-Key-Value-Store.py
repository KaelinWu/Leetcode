class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)
        
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((value,timestamp))
     

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        search = self.map[key]
        l = 0
        r = len(search)-1
        while l<=r:
            pivot = (l+r) // 2
            if search[pivot][1] > timestamp:
                
                r = pivot-1
            elif search[pivot][1] < timestamp:
                res = search[pivot][0]
                l = pivot+1
            else:
                res = search[pivot][0]
                break
        return res 




# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)