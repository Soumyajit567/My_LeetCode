# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []

        def is_leaf(node):
            return node and not node.left and not node.right

        if not is_leaf(root):
            res.append(root.val)
        
        
        node = root.left
        while node:
            if not is_leaf(node):
                res.append(node.val)
            if node.left:
                node = node.left
            else:
                node = node.right

        
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if is_leaf(node):
                    res.append(node.val)
                else:
                    if node.right:
                        stack.append(node.right)
                    if node.left:
                        stack.append(node.left)

        
        stack = []
        node = root.right
        while node:
            if not is_leaf(node):
                stack.append(node.val)
            if node.right:
                node = node.right
            else:
                node = node.left

        while stack:
            res.append(stack.pop())

        return res