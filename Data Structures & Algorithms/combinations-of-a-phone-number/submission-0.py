class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d2l = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        res = []
        if not digits:
            return res
        def recur(i, cur):
            if i == len(digits):
                res.append(cur)
                return
            for letter in d2l[digits[i]]:
                cur += letter
                recur(i + 1, cur)
                cur = cur[:-1]
        recur(0, '')
        return res