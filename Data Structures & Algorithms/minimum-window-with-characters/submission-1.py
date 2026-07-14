from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target_count = defaultdict(int)
        for c in t:
            target_count[c] += 1
        count = defaultdict(int)
        def check(count):
            for k, v in target_count.items():
                if count[k] < v:
                    return False
            return True
        l, r = 0, 0
        res = ''
        while l < len(s) and r <= len(s):
            if check(count):
                if res == '' or (r - l) < len(res):
                    res = s[l:r]
                count[s[l]] -= 1
                l += 1
            else:
                if r == len(s):
                    break
                count[s[r]] += 1
                r += 1                    
        return res
        
