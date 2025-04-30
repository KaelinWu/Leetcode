class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lower = 0
        upper = len(nums)-1
        pivot = int(upper/2)

        while lower <= upper:
            if nums[pivot] == target:
                return pivot
            elif nums[pivot] < target:
                lower = pivot + 1
                pivot = int((lower + upper)/2)
            else:
                upper = pivot - 1
                pivot = int((lower + upper)/2)
        return -1