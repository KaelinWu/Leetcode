class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        num2 = set(nums)
        
        if len(num2) != len(nums) :
            return True
        return False
        