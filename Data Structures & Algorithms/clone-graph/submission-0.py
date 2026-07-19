"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        copies = {}
        q = deque([node])
        while q:
            n = q.popleft()
            if n in copies:
                continue
            copies[n] = Node(n.val)
            for neighbor in n.neighbors:
                q.append(neighbor)
        visited = set()
        q = deque([node])
        while q:
            n = q.popleft()
            if n in visited:
                continue
            visited.add(n)
            for neighbor in n.neighbors:
                copies[n].neighbors.append(copies[neighbor])
                q.append(neighbor)
        return copies[node]