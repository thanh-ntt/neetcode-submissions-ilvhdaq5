class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_pos = {}
        for i in range(len(s) - 1, -1, -1):
            if s[i] not in last_pos:
                last_pos[s[i]] = i
        res = []
        l, r = 0, 0
        while l < len(s):
            i = l
            while i <= r:
                r = max(r, last_pos[s[i]])
                i += 1
            res.append(r - l + 1)
            l, r = i, i
        return res