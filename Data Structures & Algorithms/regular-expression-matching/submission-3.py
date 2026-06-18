class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        q = []
        for i in range(len(p)):
            if p[i] != '*':
                q.append(p[i])
            else:
                q[-1] = q[-1] + '*'
        dp = {}
                
        def check(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            elif j == len(q):
                return i == len(s)
            elif i == len(s):
                while j < len(q) and len(q[j]) == 2:
                    j += 1
                dp[(i, j)] = j == len(q)
                return dp[(i, j)]
            elif len(q[j]) == 1:
                dp[(i, j)] = q[j] in ['.', s[i]] and check(i + 1, j + 1)
                return dp[(i, j)]
            else:
                next_i = i
                while next_i < len(s) and q[j][0] in ['.', s[next_i]]:
                    if check(next_i, j + 1):
                        dp[(i, j)] = True
                        return dp[(i, j)]
                    next_i += 1
                dp[(i, j)] = check(next_i, j + 1)
                return dp[(i, j)]

        return check(0, 0)
