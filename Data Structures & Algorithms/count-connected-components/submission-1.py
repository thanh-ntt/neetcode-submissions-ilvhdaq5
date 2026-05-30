class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {}
        for u in range(n):
            graph[u] = set()
        for e in edges:
            graph[e[0]].add(e[1])
            graph[e[1]].add(e[0])
        count = 0
        visited = [False for _ in range(n)]

        def dfs(u):
            # print(f'dfs {u}')
            if visited[u]:
                return False
            visited[u] = True
            for v in graph[u]:
                dfs(v)
            return True
        
        for u in range(n):
            count += 1 if dfs(u) else 0
        return count