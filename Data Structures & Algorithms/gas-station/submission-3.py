class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        s = 0
        for i in range(n):
            s += gas[i] - cost[i]
        if s < 0:
            return -1
        s = 0
        i, j = 0, 0
        while j < n:
            s += gas[j] - cost[j]
            if s < 0:
                i = j + 1
                s = 0
            j += 1
        return i
        