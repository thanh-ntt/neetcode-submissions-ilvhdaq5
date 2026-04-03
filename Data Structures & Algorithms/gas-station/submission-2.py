class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        gain = [gas[i] - cost[i] for i in range(n)]
        if sum(gain) < 0:
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
        