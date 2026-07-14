from collections import defaultdict, deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])
        visited = set()
        parents = [-1] * n
        q = deque([(0, -1)])
        while q:
            node, parent = q.popleft()
            if node in visited:
                if parents[parent] == node:
                    continue
                else:
                    return False
            visited.add(node)
            parents[node] = parent
            for adj in graph[node]:
                q.append((adj, node))
        return len(visited) == n
