from sortedcontainers import SortedList
from collections import deque

class MKAverage:

    def __init__(self, m: int, k: int):
        self.m = m
        self.k = k
        self.queue = deque()
        self.sorted_list = SortedList()
        self.total = 0

    def addElement(self, num: int) -> None:
        # If the queue is full (reached 'm' elements), remove the oldest element.
        if len(self.queue) == self.m:
            old_num = self.queue.popleft()
            self.sorted_list.remove(old_num)
            self.total -= old_num

        # Add the new element to both the queue and the sorted list.
        self.queue.append(num)
        self.sorted_list.add(num)
        self.total += num

    def calculateMKAverage(self) -> int:
        # Ensure we've received at least 'm' elements.
        if len(self.queue) < self.m:
            return -1  # Not enough elements.

        # Calculate the modified average after ignoring the first and last 'k' elements.
        sum_ignored = sum(self.sorted_list[:self.k]) + sum(self.sorted_list[-self.k:])
        avg = (self.total - sum_ignored) // (self.m - 2 * self.k)
        return avg





# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()