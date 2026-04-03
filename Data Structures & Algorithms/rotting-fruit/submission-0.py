class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = []
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
        minutes = 0
        while len(q) > 0:
            next_q = []
            for o in q:
                for adj in [(o[0] + 1, o[1]), (o[0] - 1, o[1]), (o[0], o[1] + 1), (o[0], o[1] - 1)]:
                    if 0 <= adj[0] < m and 0 <= adj[1] < n and grid[adj[0]][adj[1]] == 1:
                        next_q.append(adj)
                        grid[adj[0]][adj[1]] = 2
            if len(next_q) > 0:
                minutes += 1
            q = next_q
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        return minutes