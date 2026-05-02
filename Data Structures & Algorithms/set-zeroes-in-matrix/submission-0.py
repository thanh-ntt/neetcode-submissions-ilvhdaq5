class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        nrows, ncols = len(matrix), len(matrix[0])
        for r in range(nrows):
            for c in range(ncols):
                if matrix[r][c] == 0:
                    for i in range(nrows):
                        if i != r and matrix[i][c] != 0:
                            matrix[i][c] = -1
                    for i in range(ncols):
                        if i != c and matrix[r][i] != 0:
                            matrix[r][i] = -1
        for r in range(nrows):
            for c in range(ncols):
                if matrix[r][c] == -1:
                    matrix[r][c] = 0