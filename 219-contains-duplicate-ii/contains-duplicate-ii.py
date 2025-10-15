class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = 0
        numset = defaultdict(int)
        for r in range(len(nums)):
            numset[nums[r]] +=1
            if r-l > k:
                numset[nums[l]] -= 1
                l+=1
            if numset[nums[r]] > 1:
                return True
        return False
            
                
