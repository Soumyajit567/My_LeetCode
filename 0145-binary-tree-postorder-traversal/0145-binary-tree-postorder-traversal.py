# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        stack = [root]
        res = []
        reverse = []
        while stack:
            node = stack.pop()
            reverse.append(node)
            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)
        
        while reverse:
            n = reverse.pop()
            res.append(n.val)
        return res
            