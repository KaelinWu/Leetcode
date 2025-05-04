class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
    
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones)> 1:
            y = heapq.heappop(stones)
            x = heapq.heappop(stones)

            z = y-x
            if z != 0:
                heapq.heappush(stones,z)
        
        if stones:
            return -stones[0]
        return 0
        
        