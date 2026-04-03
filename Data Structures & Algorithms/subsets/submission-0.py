class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur_set = set()
        def recursion(cur_set, i):
            if i == len(nums):
                res.append(list(cur_set.copy()))
            else:
                recursion(cur_set, i + 1)
                cur_set.add(nums[i])
                recursion(cur_set, i + 1)
                cur_set.remove(nums[i])
        recursion(cur_set, 0)
        return res