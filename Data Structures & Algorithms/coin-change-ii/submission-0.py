class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        dp = {}
        def com(n, i):
            if n == 0:
                return 1
            elif n < 0 or i < 0:
                return 0
            elif (n, i) in dp:
                return dp[(n, i)]
            sum = com(n - coins[i], i) + com(n, i - 1)
            dp[(n, i)] = sum
            return sum
        return com(amount, len(coins) - 1)
                
