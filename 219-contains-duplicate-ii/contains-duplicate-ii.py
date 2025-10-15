class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
       
        numset = defaultdict(int)
        for i, val in enumerate(nums):
            if val in numset and i - numset[val] <= k:
                return True
                
            
            numset[val] = i
        return False
            
                
