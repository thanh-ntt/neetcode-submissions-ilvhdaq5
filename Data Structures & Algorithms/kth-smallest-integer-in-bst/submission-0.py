# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def size(root, sizes):
            if root:
                l_size = size(root.left, sizes)
                r_size = size(root.right, sizes)
                cur_size = l_size + r_size + 1
                sizes[root.val] = cur_size
                return cur_size
            else:
                return 0
        sizes = {}
        size(root, sizes)

        def kth(root, k):
            l_size = 0 if root.left is None else sizes[root.left.val]
            if l_size == k - 1:
                return root.val
            elif l_size > k - 1:
                return kth(root.left, k)
            else:
                return kth(root.right, k - l_size - 1)
        return kth(root, k)