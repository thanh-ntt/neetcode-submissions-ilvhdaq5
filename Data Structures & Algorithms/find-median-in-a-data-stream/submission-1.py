import heapq
class MedianFinder:

    def __init__(self):
        self.rq = []
        self.lq = []
        heapq.heapify(self.rq)
        heapq.heapify_max(self.lq)

    def addNum(self, num: int) -> None:
        if not self.lq or num <= self.lq[0]:
            heapq.heappush_max(self.lq, num)
        else:
            heapq.heappush(self.rq, num)

        if len(self.lq) + 1 < len(self.rq): # balance
            mid = heapq.heappop(self.rq)
            heapq.heappush_max(self.lq, mid)
        if len(self.lq) > len(self.rq) + 1: # balance
            mid = heapq.heappop_max(self.lq)
            heapq.heappush(self.rq, mid)
        # print(f'add {num}, lq: {self.lq}, rq: {self.rq}')

    def findMedian(self) -> float:
        if len(self.lq) > len(self.rq):
            return self.lq[0]
        elif len(self.lq) < len(self.rq):
            return self.rq[0]
        else:
            return (self.lq[0] + self.rq[0]) / 2
            