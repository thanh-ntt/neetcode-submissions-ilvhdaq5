class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        a, b = newInterval[0], newInterval[1]
        res = []
        merged = False
        i = 0
        while i < n:
            o, c = intervals[i]
            if o <= a <= c or a <= o <= b:
                o = min(a, o)
                c = max(c, b)
                while i + 1 < n and intervals[i + 1][0] <= c: # merge
                    c = max(c, intervals[i + 1][1])
                    i += 1
                merged = True
            res.append((o, c))
            i += 1
        if not merged:
            idx = next((idx for idx, interval in enumerate(intervals) if a > interval[1] and (idx == len(intervals) - 1 or intervals[idx + 1][0] > b)), -1)
            res.insert(idx + 1, (a, b))
        return res
