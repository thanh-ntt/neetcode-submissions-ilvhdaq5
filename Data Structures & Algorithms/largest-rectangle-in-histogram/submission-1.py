from collections import deque

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        s = deque() # (height, index)
        left_area = [0] * n 
        for i in range(n):
            h = heights[i]
            left_i = i
            while s and s[-1][0] >= h:
                _, left_i = s.pop()
            left_area[i] = max(left_area[i], h * (i - left_i))
            s.append((h, left_i))

        s = deque()
        right_area = [0] * n 
        for i in range(n - 1, -1, -1):
            h = heights[i]
            right_i = i
            while s and s[-1][0] >= h:
                _, right_i = s.pop()
            right_area[i] = max(right_area[i], h * (right_i - i))
            s.append((h, right_i))

        max_rect = 0
        for i in range(n):
            max_rect = max(max_rect, left_area[i] + heights[i] + right_area[i])
        return max_rect