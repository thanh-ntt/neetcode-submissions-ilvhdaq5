class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        dp = {}
        total = sum(nums)
        if total % 2 == 1:
            return False
        nums = sorted(nums)
        def rc(s, i):
            if s == 0:
                return True
            if s < 0 or i >= len(nums):
                return False
            res = rc(s - nums[i], i + 1) or rc(s, i + 1)
            dp[(s, i)] = res
            return res
        return rc(total / 2, 0)
