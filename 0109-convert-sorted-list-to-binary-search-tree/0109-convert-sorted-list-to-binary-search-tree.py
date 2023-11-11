# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        values = []
        while head:
            values.append(head.val)
            head = head.next

        def convertListToBST(left, right):
            if left > right:
                return None

            mid = (left + right) // 2
            node = TreeNode(values[mid])
            node.left = convertListToBST(left, mid - 1)
            node.right = convertListToBST(mid + 1, right)

            return node

        return convertListToBST(0, len(values) - 1)