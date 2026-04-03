class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r = 0, 0
        n = len(nums)
        step = 0
        while r < n - 1:
            step += 1
            nr = 0
            for i in range(l, r + 1):
                nr = max(nr, i + nums[i])
            l = r
            r = min(n - 1, nr)
        return step