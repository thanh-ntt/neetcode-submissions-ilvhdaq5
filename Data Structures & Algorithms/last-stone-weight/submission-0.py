import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = [s for s in stones]
        heapq.heapify_max(pq)
        while pq:
            a = heapq.heappop_max(pq)
            if not pq:
                return a
            b = heapq.heappop_max(pq)
            if a != b:
                heapq.heappush_max(pq, abs(a - b))
        return 0