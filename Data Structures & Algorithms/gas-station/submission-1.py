class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        for i in range(n):
            sum = 0
            for idx in range(i, i + n):
                j = idx % n
                sum += gas[j]
                sum -= cost[j]
                if sum < 0:
                    break
            if sum >= 0:
                return i
        return -1