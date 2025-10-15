class MyCircularQueue:

    def __init__(self, k: int):
        self.que = [0] * k

        self.head = 0
        self.capacity = k
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.que[(self.head + self.size) % self.capacity] = value
        self.size +=1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        self.head = (self.head+1)%self.capacity
        self.size -=1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.que[self.head]
    

    def Rear(self) -> int:
        if self.isEmpty():
            return -1

        return self.que[(self.head + self.size - 1)%self.capacity]
        
    def isEmpty(self) -> bool:
        if self.size == 0:
            return True
        return False

    def isFull(self) -> bool:
        if self.size == self.capacity:
            return True
        return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()