# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # in-order traversal
        res = -1000
        def dfs(n1) -> int:
            s = n1.val
            left = dfs(n1.left) if n1.left else -1000
            right = dfs(n1.right) if n1.right else -1000
            max_sum = max([s, s + left, s + right])
            # print(f'dfs {n1.val} -> max_sum = {max_sum}')
            nonlocal res
            res = max([res, max_sum, s + left + right])
            return max_sum
        
        dfs(root)
        return res