class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        coins.sort()
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in range(n - 1, -1, -1):
            for a in range(amount + 1):
                if a >= coins[i]:
                    dp[a] = dp[a] + dp[a - coins[i]]
        return dp[amount]