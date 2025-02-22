# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        stack = []
        i = 0
        n = len(traversal)
        
        while i < n:
            level = 0
            while i < n and traversal[i] == '-':
                level += 1
                i += 1
                
            start = i
            while i < n and traversal[i].isdigit():
                i += 1
            value = int(traversal[start:i])
            
            node = TreeNode(value)
            
            while len(stack) > level:
                stack.pop()
                
            if stack:
                parent = stack[-1]
                if parent.left is None:
                    parent.left = node
                else:
                    parent.right = node
            
            stack.append(node)
        
        return stack[0] if stack else None