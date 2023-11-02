# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        stack = [(root, False)]
        sum_count = {root: [0, 0]}
        
        while stack:
            node, visited = stack.pop()
            
            if visited:
                left_sum = sum_count[node.left][0] if node.left else 0
                left_count = sum_count[node.left][1] if node.left else 0
                
                right_sum = sum_count[node.right][0] if node.right else 0
                right_count = sum_count[node.right][1] if node.right else 0
                
                sum_count[node] = [left_sum + right_sum + node.val, left_count + right_count + 1]
            else:
                stack.append((node, True))
                if node.left:
                    sum_count[node.left] = [0, 0]
                    stack.append((node.left, False))
                if node.right:
                    sum_count[node.right] = [0, 0]
                    stack.append((node.right, False))
                    
        res = 0
        stack = [root]
        
        while stack:
            node = stack.pop()
            
            if node.val == sum_count[node][0] // sum_count[node][1]:
                res += 1
                
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
                
        return res