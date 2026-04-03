class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        arr = sorted(intervals)
        res = []
        i = 0
        while i < len(arr):
            r = arr[i][1]
            j = i + 1
            while j < len(arr) and arr[j][0] <= r:
                r = max(r, arr[j][1])
                j += 1
            res.append([arr[i][0], r])
            i = j
        return res
