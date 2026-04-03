# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(r, n, trace, res):
            if r is None:
                return
            trace.append(r)
            if r.val == n.val:
                res.extend(trace)
            else:
                dfs(r.left, n, trace, res)
                dfs(r.right, n, trace, res)
            trace.pop()
        trace_p, trace_q = [], []
        dfs(root, p, [], trace_p)
        dfs(root, q, [], trace_q)
        for node in trace_p[::-1]:
            if any(e.val == node.val for e in trace_q):
                return node
        return root