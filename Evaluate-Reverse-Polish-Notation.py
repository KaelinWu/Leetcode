class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        nums = deque()
        for token in tokens:
        
            if token == \*\:
                num1 = nums.pop()
                num2 = nums.pop()
                nums.append(num2*num1)
                
            elif token == \/\:
                num1 = nums.pop()
                num2 = nums.pop()
                nums.append(int(num2/num1))
            elif token == \+\:
                num1 = nums.pop()
                num2 = nums.pop()
                nums.append(num2+num1)
            elif token == \-\:
                num1 = nums.pop()
                num2 = nums.pop()
                nums.append(num2-num1)
            else:
                nums.append(int(token))
        return nums.pop()
            
                