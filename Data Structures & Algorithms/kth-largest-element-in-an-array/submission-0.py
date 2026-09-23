import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = list(nums)
        heapq.heapify_max(pq)
        res = nums[0]
        while pq and k > 0:
            res = heapq.heappop_max(pq)
            k -= 1
        return res