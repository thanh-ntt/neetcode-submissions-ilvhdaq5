class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        res = [-1 for _ in range(10_001)]
        for interval in intervals:
            length = interval[1] - interval[0] + 1
            for i in range(interval[0], interval[1] + 1):
                if res[i] == -1 or res[i] > length:
                    res[i] = length
        return [res[q] for q in queries]
