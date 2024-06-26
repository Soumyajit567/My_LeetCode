# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def inorderTraversal(root):
            stack = []
            result = []
            current = root
            while current or stack:
                while current:
                    stack.append(current)
                    current = current.left
                current = stack.pop()
                result.append(current.val)
                current = current.right
            return result

        sorted_values = inorderTraversal(root)


        def sortedArrayToBST(nums):
            if not nums:
                return None
            
            stack = [(0, len(nums) - 1, None, None, True)]
            root = None
            
            while stack:
                left, right, parent, is_left, is_root = stack.pop()
                if left > right:
                    continue
                
                mid = (left + right) // 2
                node = TreeNode(nums[mid])
                
                if is_root:
                    root = node
                else:
                    if is_left:
                        parent.left = node
                    else:
                        parent.right = node
                
                stack.append((left, mid - 1, node, True, False))
                stack.append((mid + 1, right, node, False, False))
            
            return root
        
        return sortedArrayToBST(sorted_values)