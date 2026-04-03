class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        # 1  2  3  4
        # 5  6  7  8
        # 9  10 11 12
        # 13 14 15 16
        m, n = len(matrix), len(matrix[0])
        u, d, l, r = 0, m - 1, 0, n - 1
        while True:
            # east
            for j in range(l, r + 1):
                res.append(matrix[u][j])
            u += 1
            if u > d:
                return res
            for i in range(u, d + 1):
                res.append(matrix[i][r])
            r -= 1
            if l > r:
                return res
            for j in range(r, l - 1, -1):
                res.append(matrix[d][j])
            d -= 1
            if u > d:
                return res
            for i in range(d, u - 1, -1):
                res.append(matrix[i][l])
            l += 1
            if l > r:
                return res
        return res
            

