class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def add(a, b) -> str:
            # print(f'add {a}, {b}')
            if len(a) < len(b):
                a, b = b, a
            mem = 0
            s = ''
            for i in range(len(a)):
                res = mem + int(a[-i - 1])
                if i < len(b):
                    res += int(b[-i - 1])
                if res >= 10:
                    mem = 1
                    res -= 10
                else:
                    mem = 0
                s = str(res) + s
            if mem > 0:
                s = '1' + s
            return s
        
        def mul(a, b) -> str:
            # print(f'mul {a}, {b}')
            if len(a) < len(b):
                a, b = b, a
            if len(b) > 1:
                # print(f' call {a}, {b[:-1]}')
                return add(mul(a, b[:-1]) + '0', mul(a, b[-1]))
            else:
                mem = 0
                s = ''
                for i in range(len(a) - 1, -1, -1):
                    res = mem + int(b[0]) * int(a[i])
                    mem = res // 10
                    s = str(res % 10) + s
                if mem > 0:
                    s = str(mem) + s
                # print(f'mul {a}, {b} -> {s}')
                while s[0] == '0' and len(s) > 1:
                    s = s[1:]
                return s
        
        return mul(num1, num2)