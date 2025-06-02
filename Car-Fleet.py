class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = 0
        cars = [(p,s) for p,s in zip(position,speed)]
        cars = sorted(cars, key=lambda x: -x[0])
        print(cars)
        prev_time = 0
        for p,s in cars:
            time = (target-p)/s
            if time > prev_time:
                res+=1
                prev_time = time
        return res
            
            


