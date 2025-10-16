class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        
        lst = SortedList()
        res = []
        for i in range(len(nums)):
            lst.add(nums[i])
            if len(lst) > k:
                lst.remove(nums[i-k])            
            if len(lst) == k:
                if k%2 == 0:
                    res.append((lst[k//2-1] + lst[k//2])/2)
                else:
                    res.append(lst[k//2])
           
        return res
