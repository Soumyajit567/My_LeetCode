# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0
        stack = [(root, 1)]
        level_sums = {}
        while stack:
            node, level = stack.pop()
            level_sums[level] = level_sums.get(level, 0) + node.val
            if node.left is not None:
                stack.append((node.left, level + 1))
            if node.right is not None:
                stack.append((node.right, level + 1))

        sorted_sums = sorted(level_sums.values(), reverse=True)
        return sorted_sums[k - 1] if k <= len(sorted_sums) else -1