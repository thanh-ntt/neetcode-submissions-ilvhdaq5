class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        def check(visited, i, r, c):
            if i == len(word):
                return True
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False
            if visited[r][c] or board[r][c] != word[i]:
                return False
            visited[r][c] = True
            res = check(visited, i + 1, r + 1, c) or check(visited, i + 1, r - 1, c) or check(visited, i + 1, r, c + 1) or check(visited, i + 1, r, c - 1)
            visited[r][c] = False
            return res
        visited = [[False] * cols for _ in range(rows)]
        for row in range(rows):
            for col in range(cols):
                if check(visited, 0, row, col):
                    return True
        return False
