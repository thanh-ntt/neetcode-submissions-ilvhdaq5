class Solution:
    def reverse(self, x: int) -> int:
        x_str = str(x)
        reverse = ''
        for i in range(len(x_str)):
            reverse = x_str[i] + reverse
        if reverse[-1] == '-':
            reverse = '-' + reverse[:-1]
        if -2**31 <= int(reverse) <= 2**31 - 1:
            return int(reverse)
        else:
            return 0