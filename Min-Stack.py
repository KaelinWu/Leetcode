class MinStack:

    def __init__(self):
        self.stack = []
      

    def push(self, val: int) -> None:
        if self.stack:
            min_val = self.stack[-1][1]
        else:
            min_val = None
        if min_val == None or min_val>val:
            min_val = val
        self.stack.append([val,min_val])

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]
        return None
        

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]
        return None

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()