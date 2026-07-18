from collections import defaultdict
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [[] for _ in range(n)]
        for f in flights:
            graph[f[0]].append((f[1], f[2]))
        inf = 1_000_000
        dist = [inf for _ in range(n)]
        dist[src] = 0
        connected = set([src])
        for i in range(k + 1):
            new_connected = set()
            new_dist = list(dist)
            for u in connected:
                for v, e in graph[u]:
                    if dist[u] + e < dist[v]:
                        new_dist[v] = dist[u] + e
                    new_connected.add(v)
            dist = new_dist
            connected |= new_connected
            # print(f'connected: {connected}, dist: {dist}')
        return dist[dst] if dist[dst] < 1_000_000 else -1


