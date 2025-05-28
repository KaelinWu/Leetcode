class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        numbers = set(nums)
       
        
        
        max_len = 1
        for num in numbers:
            curr_len = 1
            if num-1 not in numbers:
                search = num + 1
                while search in numbers:
                    curr_len+=1
                    search +=1
                max_len = max(max_len,curr_len)
        return max_len


        


