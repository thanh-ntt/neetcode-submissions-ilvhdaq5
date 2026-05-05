class Solution {
    public int coinChange(int[] coins, int amount) {
        Map<Integer, Integer> memo = new HashMap<>();
        // Arrays.sort(coins, (a, b) -> b - a);
        int res = recur(coins, amount, memo);
        if (res >= 10000) return -1;
        else return res;
    }
    public int recur(int[] coins, int amount, Map<Integer, Integer> memo) {
        if (amount < 0) return 10000;
        else if (amount == 0) return 0;
        if (memo.containsKey(amount)) {
            return memo.get(amount);
        }
        int minCount = 10000;
        for (int c : coins) {
            int count = recur(coins, amount - c, memo);
            minCount = Math.min(minCount, count);
        }
        minCount++;
        memo.put(amount, minCount);
        // System.out.println(amount + " -> " + minCount);
        return minCount;
    }
}
