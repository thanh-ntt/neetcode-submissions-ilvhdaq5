class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        # memo = [ [2_000_000]* n for i in range(n)]
        max_s = -2_000_000
        for i in range(n):
            s = 0
            for j in range(i, n):
                s += nums[j]
                if s > max_s:
                    max_s = s
        return max_s
                