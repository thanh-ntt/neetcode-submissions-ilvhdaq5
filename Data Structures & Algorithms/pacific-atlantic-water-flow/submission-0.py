from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # bfs from ocean, find overlap
        m, n = len(heights), len(heights[0])
        pa = deque()
        pa.extend([(0, i) for i in range(n)])
        pa.extend([(i, 0) for i in range(m)])
        at = deque()
        at.extend([(m - 1, i) for i in range(n)])
        at.extend([(i, n - 1) for i in range(m)])

        def bfs(q):
            reach = set()
            while len(q) > 0:
                cur = q.popleft()
                reach.add(cur)
                for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    i = cur[0] + d[0]
                    j = cur[1] + d[1]
                    if 0 <= i < m and 0 <= j < n and heights[i][j] >= heights[cur[0]][cur[1]] and (i, j) not in reach:
                        q.append((i, j))
            return reach

        pa_reach = bfs(pa)
        at_reach = bfs(at)
        both_reach = pa_reach.intersection(at_reach)
        return list(both_reach)