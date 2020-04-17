import heapq
class Solution:
    def __init__(self):
        self.count = 0
        self.max_heap = []
        self.min_heap = []

    def Insert(self, num):
        self.count += 1
        heapq.heappush(self.max_heap, -num)
        max_heap_top = heapq.heappop(self.max_heap)
        heapq.heappush(self.min_heap, -max_heap_top)

        if self.count & 1:
            min_heap_top = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -min_heap_top)

    def GetMedian(self, s):
        if self.count & 1:
            return -self.max_heap[0]
        else:
            return (self.min_heap[0] - self.max_heap[0]) / 2.0

