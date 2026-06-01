class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows, cols = len(grid), len(grid[0])
        max_area = 0
        visited = {}
        def dfs(i, j):
            if (i, j) in visited or grid[i][j] == 0:
                return 0
            visited[(i, j)] = True
            area = 1
            for d in dirs:
                r, c = i + d[0], j + d[1]
                if 0 <= r < rows and 0 <= c < cols:
                    area += dfs(r, c)
            return area
        
        for i in range(rows):
            for j in range(cols):
                max_area = max(max_area, dfs(i, j))
        return max_area