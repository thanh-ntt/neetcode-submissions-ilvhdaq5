class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        min_op = [[1000 for col in range(len(word2))] for row in range(len(word1))]
        def minD(i, j):
            if j == len(word2):
                return len(word1) - i
            if i == len(word1):
                return len(word2) - j
            if min_op[i][j] < 1000:
                return min_op[i][j]
            if word1[i] == word2[j]:
                res = minD(i + 1, j + 1)
            else:
                res = 1 + min(minD(i + 1, j + 1), minD(i + 1, j), minD(i, j + 1))
            min_op[i][j] = res
            return res
        return minD(0, 0)