class Solution {
    public int findMin(int[] nums) {
        return recur(nums, 0, nums.length - 1);
    }

    public int recur(int[] nums, int left, int right) {
        int mid = (left + right) / 2;
        if (nums[left] <= nums[mid]) {
            if (nums[mid] <= nums[right]) {
                return nums[left];
            } else {
                return recur(nums, mid + 1, right);
            }
        } else {
            return recur(nums, left, mid);
        }
    }
}
