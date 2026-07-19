from collections import defaultdict, deque
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = defaultdict(set)
        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                a, b = words[i], words[j]
                k = 0
                while k < min(len(a), len(b)) and a[k] == b[k]:
                    k += 1
                if k < min(len(a), len(b)):
                    graph[a[k]].add(b[k])
                else:
                    if len(a) > len(b):
                        # print(f'a: {a}, b: {b}')
                        return ''
        all_chars = set()
        for w in words:
            all_chars.update(w[:])
        indegrees = {c: 0 for c in all_chars}
        for u, adj in graph.items():
            for v in adj:
                indegrees[v] += 1
        # print(f'all_chars: {all_chars}')
        # print(f'indegrees: {indegrees}')
        q = deque([c for c in indegrees.keys() if indegrees[c] == 0])
        res = ''
        while q:
            u = q.popleft()
            res += u
            for v in graph[u]:
                indegrees[v] -= 1
                if indegrees[v] == 0:
                    q.append(v)
        return res if len(res) == len(all_chars) else ''