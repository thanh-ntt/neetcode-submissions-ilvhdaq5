from queue import PriorityQueue

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        # print(f'start: {dp}')
        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        
        def dfs(i, j):
            print(f'call {i}, {j}')
            if dp[i][j] > 0:
                return dp[i][j]
            max_length = 0
            for d in dirs:
                r, c = i + d[0], j + d[1]
                if 0 <= r < rows and 0 <= c < cols and matrix[i][j] < matrix[r][c]:
                    max_length = max(max_length, dfs(r, c))
            dp[i][j] = 1 + max_length
            # print(f'loop: {dp}')
            return dp[i][j]
        
        pq = PriorityQueue()
        for i in range(rows):
            for j in range(cols):
                pq.put((-matrix[i][j], i, j))
        while not pq.empty():
            pos = pq.get()
            # print(f'pos: {pos}')
            dfs(pos[1], pos[2])

        res = 0
        for r in dp:
            res = max(res, max(r))
        # print(f'end: {dp}')
        return res