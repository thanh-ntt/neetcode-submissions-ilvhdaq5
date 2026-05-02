class Solution:
    def numDecodings(self, s: str) -> int:
        # f(s[0:n]) = f(s[1:n]) + f(s[2:n])
        n = len(s)
        dp = [0] * n
        for i in range(n - 1, -1, -1):
            if s[i] == '0':
                continue
            if i == n - 1:
                dp[i] = 1
            else:
                dp[i] = dp[i + 1]
                if 0 < int(s[i:i+2]) < 27:
                    dp[i] += dp[i + 2] if i < n - 2 else 1
        print(dp)
        return dp[0]