from collections import defaultdict, deque
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = max(max(e[0], e[1]) for e in edges)
        graph = defaultdict(list)
        in_degrees = [0] * (n + 1)
        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])
            in_degrees[e[0]] += 1
            in_degrees[e[1]] += 1
        q = deque([i for i in range(1, n + 1) if in_degrees[i] == 1])
        while q:
            u = q.popleft()
            for v in graph[u]:
                in_degrees[v] -= 1
                if in_degrees[v] == 1:
                    q.append(v)
        cycles = {i for i in range(1, n + 1) if in_degrees[i] > 1}
        for i in range(len(edges) - 1, -1, -1):
            if edges[i][0] in cycles and edges[i][1] in cycles:
                return edges[i]
        return []