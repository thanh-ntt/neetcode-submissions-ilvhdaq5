class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def minD(word1, word2, i, j):
            # print(f'minD {i}, {j}')
            if j == len(word2):
                return len(word1) - i
            if i == len(word1):
                return len(word2) - j
            if word1[i] == word2[j]:
                return minD(word1, word2, i + 1, j + 1)
            else:
                # print(f'+1')
                return 1 + min(minD(word1, word2, i + 1, j + 1), minD(word1, word2, i + 1, j), minD(word1, word2, i, j + 1))
        return minD(word1, word2, 0, 0)