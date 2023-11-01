# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root]
        hashmap = {}
        res = []
        while stack:
            node = stack.pop()
            if node:
                if node.val not in hashmap:
                    hashmap[node.val] = 1
                else:
                    hashmap[node.val] += 1
                if node.left is not None:
                    stack.append(node.left)
                if node.right is not None:
                    stack.append(node.right)
        k = max(val for key, val in hashmap.items())
        for key, val in hashmap.items():
            if val == k:
                res.append(key)
        return res


        
