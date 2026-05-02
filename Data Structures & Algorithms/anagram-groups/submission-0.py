class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sort each string, anagram = same sorted string
        a2s = {}
        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s not in a2s:
                a2s[sorted_s] = []
            a2s[sorted_s].append(s)
        res = []
        for v in a2s.values():
            res.append(v)
        return res