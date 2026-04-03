class Solution:
    def isValid(self, s: str) -> bool:
        def match(l, r):
            if l == '(':
                return r == ')'
            elif l == '{':
                return r == '}'
            elif l == '[':
                return r == ']'
            else:
                return False
        stack = []
        for c in s:
            if c in {'(', '{', '['}:
                stack.append(c)
            elif len(stack) > 0:
                left_char = stack.pop()
                if not match(left_char, c):
                    return False
            else:
                return False
        return len(stack) == 0
