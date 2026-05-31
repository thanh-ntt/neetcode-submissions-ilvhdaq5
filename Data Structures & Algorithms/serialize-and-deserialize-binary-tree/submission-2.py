# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # print(f'call serialize')
        q = deque()
        q.append(root)
        s = ''
        while q:
            n1 = q.popleft()
            if n1:
                s += str(n1.val)
                q.append(n1.left)
                q.append(n1.right)
            else:
                s += 'null'
            s += ' '
        print(f'serialize: {s.strip()}')
        return s.strip()
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # print(f'call deserialize')
        def decode(s: str) -> Optional[TreeNode]:
            if s == 'null':
                return None
            else:
                return TreeNode(int(s))
        q1 = deque([decode(n1) for n1 in data.split(' ')])
        q2 = deque()
        if not q1:
            return None
        root = q1.popleft()
        q2.append(root)
        while q1 and q2:
            n1 = q2.popleft()
            l, r = q1.popleft(), q1.popleft()
            n1.left, n1.right = l, r
            if l:
                q2.append(l)
            if r:
                q2.append(r)
        return root

        
