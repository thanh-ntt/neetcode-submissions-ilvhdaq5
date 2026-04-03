class Solution:
    def jump(self, nums: List[int]) -> int:
        # jumps: min # jumps needed to reach the end
        # jumps[i] = min(1 if nums[i] >= len - i - 1; 1 + min(jumps[i+1], ..., jumps[i+nums[i]]))
        n = len(nums)
        jumps = [n] * n
        jumps[n - 1] = 0
        for i in range(n - 2, -1, -1):
            if nums[i] >= n - i - 1:
                jumps[i] = 1
            else:
                for j in range(i + 1, i + nums[i] + 1):
                    jumps[i] = min(jumps[i], 1 + jumps[j])
        return jumps[0]