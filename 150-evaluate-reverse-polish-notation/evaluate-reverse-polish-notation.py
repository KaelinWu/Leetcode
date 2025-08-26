class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []

        for token in tokens:
            if token == "+":
                num2 = int(nums.pop())
                num1 = int(nums.pop())
                nums.append(num1+num2)
            elif token == "-":
                num2 = int(nums.pop())
                num1 = int(nums.pop())
                nums.append(num1-num2)
            elif token == "/":
                num2 = int(nums.pop())
                num1 = int(nums.pop())
                nums.append(num1/num2)
            elif token == "*":
                num2 = int(nums.pop())
                num1 = int(nums.pop())
                nums.append(num1*num2)
            else:
                nums.append(token)
        return int(nums.pop())

            