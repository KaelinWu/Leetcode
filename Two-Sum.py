class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in my_dict:
                return [i, my_dict[diff]]
            my_dict[nums[i]] = i
        return False
           

        