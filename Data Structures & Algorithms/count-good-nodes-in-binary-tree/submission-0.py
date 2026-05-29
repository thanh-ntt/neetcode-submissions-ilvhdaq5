# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(cur, max_val) -> int:
            if not cur:
                return 0
            good_node = 0
            if cur.val >= max_val:
                good_node = 1
                max_val = cur.val
            return good_node + dfs(cur.left, max_val) + dfs(cur.right, max_val)
        return dfs(root, -100)