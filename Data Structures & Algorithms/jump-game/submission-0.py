class Solution:
    def canJump(self, nums: List[int]) -> bool:
        end = 0
        for i in range(len(nums)):
            if i > end:
                # print('break')
                break
            if nums[i] > 0:
                end = max(end, i + nums[i])
        # print(end)
        return end >= len(nums) - 1