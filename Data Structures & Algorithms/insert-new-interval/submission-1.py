class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ranges = deque([i for i in intervals])
        a, b = newInterval[0], newInterval[1]
        res = []
        merged = False
        while ranges:
            o, c = ranges.popleft()
            if o <= a <= c or a <= o <= b:
                print(f'overlap: (o, c) = ({o}, {c}), (a, b) = ({a}, {b})')
                o = min(a, o)
                c = max(c, b)
                while ranges and ranges[0][0] <= c: # merge
                    merged_interval = ranges.popleft()
                    c = max(c, merged_interval[1])
                    print(f'merge: {merged_interval}, c -> {c}')
                merged = True
            res.append((o, c))
        if not merged:
            idx = next((idx for idx, interval in enumerate(intervals) if a > interval[1] and (idx == len(intervals) - 1 or intervals[idx + 1][0] > b)), -1)
            res.insert(idx + 1, (a, b))
        return res
