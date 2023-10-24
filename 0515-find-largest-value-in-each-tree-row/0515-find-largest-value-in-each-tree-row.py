# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = deque([(root, 0)])
        hashmap = {}
        res = []
        while queue:
            size = len(queue)
            for _ in range(size):
                node, level = queue.popleft()
                if level not in hashmap:
                    hashmap[level] = [node.val]
                else:
                    hashmap[level].append(node.val)            

                if node:
                    if node.left is not None:
                        queue.append((node.left, level + 1))
                    if node.right is not None:
                        queue.append((node.right, level + 1))
        for key, arr in hashmap.items():
            max_val = float("-inf")
            for ele in arr:
                max_val = max(max_val, ele)
            res.append(max_val)
        return res