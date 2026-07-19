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
        def bfs(node, visited, copies, is_first_pass=False):
            q = deque([node])
            while q:
                n = q.popleft()
                if n in visited:
                    continue
                visited.add(n)
                if is_first_pass:
                    copies[n] = Node(n.val)
                for neighbor in n.neighbors:
                    if not is_first_pass:
                        copies[n].neighbors.append(copies[neighbor])
                    q.append(neighbor)
        copies = {}
        bfs(node, set(), copies, True)
        bfs(node, set(), copies)
        return copies[node]