class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        heap = defaultdict(list)
        for row in range(len(nums)):
            for col in range(len(nums[0])):
                heapq.heappush(heap[row],-nums[row][col])
        res = 0
        
        for col in range(len(nums[0])):
            largest = 0
            for i in range(len(nums)):
                new = -heapq.heappop(heap[i])
                if new > largest:
                    largest = new
            res+= largest
        return res
