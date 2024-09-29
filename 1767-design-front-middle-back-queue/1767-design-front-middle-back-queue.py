class FrontMiddleBackQueue:

    def __init__(self):
        self.queue = []

    def pushFront(self, val: int) -> None:
        self.queue.insert(0, val)
        

    def pushMiddle(self, val: int) -> None:
        mid = len(self.queue) // 2
        self.queue.insert(mid, val)
        

    def pushBack(self, val: int) -> None:
        self.queue.append(val)

    def popFront(self) -> int:
        if len(self.queue) > 0:
            x = self.queue.pop(0)
            return x
        else:
            return -1

    def popMiddle(self) -> int:
        if len(self.queue) > 0:
            mid = (len(self.queue) - 1) // 2
            x = self.queue.pop(mid)
            return x
        else:
            return -1
        

    def popBack(self) -> int:
        if len(self.queue) > 0:
            x = self.queue.pop()
            return x
        else:
            return -1
        
        


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()