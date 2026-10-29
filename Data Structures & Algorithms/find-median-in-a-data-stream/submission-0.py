import heapq


class MedianFinder:
    def __init__(self):
        self.left = []   # max heap
        self.right = []  # min heap

    def addNum(self, num: int) -> None:
        if not self.left and not self.right:
            heapq.heappush(self.left, -num)
            return

        if self.right and self.right[0] < num:
            heapq.heappush(self.right, num)
        else:
            heapq.heappush(self.left, -num)
        
        if len(self.left) == len(self.right) + 2:
            val = heapq.heappop(self.left)
            heapq.heappush(self.right, -val)
        if len(self.right) == len(self.left) + 2:
            val = heapq.heappop(self.right)
            heapq.heappush(self.left, -val)

    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            return (-self.left[0] + self.right[0]) / 2.0
        elif len(self.left) > len(self.right):
            return -self.left[0]
        else:
            return self.right[0]
        