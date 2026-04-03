class Solution:
    def hammingWeight(self, n: int) -> int:
        # print(n)
        sum = 0
        while n > 0:
            sum += n & 1
            n = n >> 1
        return sum