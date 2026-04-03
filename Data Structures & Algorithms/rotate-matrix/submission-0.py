class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for r in range(math.ceil(n/2)):
            for c in range(math.floor(n/2)):
                temp = matrix[r][c]
                matrix[r][c] = matrix[n - c - 1][r]
                matrix[n - c - 1][r] = matrix[n - r - 1][n - c - 1]
                matrix[n - r - 1][n - c - 1] = matrix[c][n - r - 1]
                matrix[c][n - r - 1] = temp

