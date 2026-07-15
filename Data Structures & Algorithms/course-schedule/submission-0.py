from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        indegrees = [0] * numCourses
        for e in prerequisites:
            graph[e[0]].append(e[1])
            indegrees[e[1]] += 1
        q = deque([u for u in range(numCourses) if indegrees[u] == 0])
        while q:
            u = q.popleft()
            for v in graph[u]:
                indegrees[v] -= 1
                if indegrees[v] == 0:
                    q.append(v)
        return all(indegrees[u] == 0 for u in range(numCourses))