class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        minHeap = []
        heapq.heappush(minHeap, (0, k))
        graph = {u: {} for u in range(1, n + 1)}
        for time in times:
            graph[time[0]][time[1]] = time[2]
        dist = {}
        while len(minHeap) > 0:
            d, u = heapq.heappop(minHeap)
            if u not in dist or dist[u] > d:
                dist[u] = d
                for v, t in graph[u].items():
                    heapq.heappush(minHeap, (d + t, v))
        return max(dist.values()) if len(dist) == n else -1
