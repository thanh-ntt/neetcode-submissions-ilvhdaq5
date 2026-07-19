from collections import defaultdict, deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        graph = defaultdict(list)
        for w in [beginWord, *words]: # O(n * m)
            for c in range(len(w)): # O(m)
                for i in range(26): # O(1)
                    next_c = chr(ord('a') + i)
                    next_w = w[:c] + next_c
                    if c < len(w) - 1:
                        next_w += w[(c + 1):]
                    if next_c != w[c] and next_w in words:
                        graph[w].append(next_w)
        visited = set()
        q = deque([(beginWord, 1)])
        while q:
            w, steps = q.popleft()
            if w in visited:
                continue
            visited.add(w)
            if w == endWord:
                return steps
            for next_w in graph[w]:
                q.append((next_w, steps + 1))
        return 0