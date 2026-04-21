class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] leftProducts = new int[n];
        int[] rightProducts = new int[n];
        int cur = 1;
        for (int i = 0; i < n; i++) {
            leftProducts[i] = cur;
            cur *= nums[i];
        }
        cur = 1;
        for (int i = n - 1; i >= 0; i--) {
            rightProducts[i] = cur;
            cur *= nums[i];
        }
        int[] results = new int[n];
        for (int i = 0; i < n; i++) {
            results[i] = leftProducts[i] * rightProducts[i];
        }
        return results;
    }
}  
