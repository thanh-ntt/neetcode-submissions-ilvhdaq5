class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        def traverse(i, j, dist):
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            if dist == 0 or grid[i][j] > dist:
                grid[i][j] = dist
                traverse(i + 1, j, dist + 1)
                traverse(i - 1, j, dist + 1)
                traverse(i, j + 1, dist + 1)
                traverse(i, j - 1, dist + 1)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    traverse(i, j, 0)