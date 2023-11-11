# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        min_depth = float("inf")
        stack = [(root, 1)]

        while stack:
            node, level = stack.pop()
            if node.left is not None:
                stack.append((node.left, level + 1))
            if node.right is not None:
                stack.append((node.right, level + 1))
            if not node.left and not node.right:
                min_depth = min(min_depth, level)
        return min_depth
