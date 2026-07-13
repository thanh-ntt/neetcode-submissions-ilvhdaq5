from collections import deque
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        def swim(h):
            if grid[0][0] > h:
                return False
            visited = {}
            q = deque([(0, 0)])
            while q:
                i, j = q.popleft()
                if i == len(grid) - 1 and j == len(grid[0]) - 1:
                    return True
                if (i, j) in visited:
                    continue
                visited[(i, j)] = True
                for d in dirs:
                    r, c = i + d[0], j + d[1]
                    if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] <= h:
                        q.append((r, c))
            return False
        max_h = 0
        for r in range(len(grid)):
            max_h = max(max_h, max(grid[r]))
        res = max_h
        l, r = 0, max_h
        while l <= r:
            m = (l + r) // 2
            if swim(m):
                res = m
                r = m - 1
            else:
                l = m + 1
        return res