class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        q = []
        for i in range(len(p)):
            if p[i] != '*':
                q.append(p[i])
            else:
                q[-1] = q[-1] + '*'
        # print(f's: {s}, q: {q}')
                
        def check(i, j):
            # print(f'check {i}, {j}')
            if j == len(q):
                return i == len(s)
            elif i == len(s):
                while j < len(q) and len(q[j]) == 2:
                    j += 1
                return j == len(q)
            elif len(q[j]) == 1:
                return q[j] in ['.', s[i]] and check(i + 1, j + 1)
            else:
                next_i = i
                while next_i < len(s) and q[j][0] in ['.', s[next_i]]:
                    if check(next_i, j + 1):
                        return True
                    next_i += 1
                return check(next_i, j + 1)

        return check(0, 0)
