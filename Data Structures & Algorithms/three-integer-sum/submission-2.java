class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();
        Set<String> tripletSet = new HashSet<>();
        for (int i = 0; i < nums.length; i++) {
            int l = 0;
            int r = nums.length - 1;
            while (l < r) {
                if (l == i) l++;
                else if (r == i) r--;
                else {
                    int sum = nums[l] + nums[r] + nums[i];
                    if (sum > 0) r--;
                    else if (sum < 0) l++;
                    else {
                        ArrayList<Integer> triplet = new ArrayList<>(List.of(nums[l], nums[r], nums[i]));
                        Collections.sort(triplet);
                        if (!tripletSet.contains(triplet.toString())) {
                            tripletSet.add(triplet.toString());
                            res.add(triplet);
                        }
                        l++;
                        r--;
                    }
                }
            }
        }
        return res;
    }
}
