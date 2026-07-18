from collections import defaultdict
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        inf = 1_000_000
        dist = [inf for _ in range(n)]
        dist[src] = 0
        for i in range(k + 1):
            new_dist = list(dist)
            for u, v, e in flights:
                if dist[u] + e < new_dist[v]:
                    new_dist[v] = dist[u] + e
            dist = new_dist
        return dist[dst] if dist[dst] < inf else -1


