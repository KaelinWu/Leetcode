class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            numbers = set()

            for i in range(1,int(num**0.5)+1):
                if num % i == 0:
                    numbers.add(i)
                    numbers.add(num//i)
                if len(numbers)>4:
                    break
            if len(numbers) == 4:
                res += sum(numbers)
        
        return res
        
