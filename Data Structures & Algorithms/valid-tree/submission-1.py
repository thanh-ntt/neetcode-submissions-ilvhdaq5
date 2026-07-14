from collections import defaultdict, deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])
        visited = set()
        used_edges = set()
        q = deque([(0, -1)])
        while q:
            node, parent = q.popleft()
            if node in visited:
                if (node, parent) in used_edges:
                    continue
                else:
                    print(f'node: {node}, parent: {parent}, visited: {visited}, used_edges: {used_edges}')
                    return False
            visited.add(node)
            used_edges.add((parent, node))
            for adj in graph[node]:
                q.append((adj, node))
        return len(visited) == n
