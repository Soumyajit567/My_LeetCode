class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = []
        self.k = k

    def enQueue(self, value: int) -> bool:
        if len(self.queue) < self.k:
            self.queue.append(value)
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if len(self.queue) > 0:
            self.queue.pop(0)
            return True
        else:
            return False
        

    def Front(self) -> int:
        if len(self.queue) > 0:
            return self.queue[0]
        else:
            return -1
        

    def Rear(self) -> int:
        if len(self.queue) > 0:
            return self.queue[-1]
        else:
            return -1
        

    def isEmpty(self) -> bool:
        return len(self.queue) == 0
        

    def isFull(self) -> bool:
        return len(self.queue) == self.k
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()