# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head

        # Helper function to check the length of the linked list
        def get_length(node):
            length = 0
            while node:
                length += 1
                node = node.next
            return length

        def reverse_k_nodes(prev, start, k):
            cur = start
            stack = []
            while k > 0 and cur:
                stack.append(cur)
                cur = cur.next
                k -= 1

            # If there are not enough nodes left to reverse
            if len(stack) < k:
                return start  # Return the original start if cannot reverse

            tail = stack[0]
            while stack:
                prev.next = stack.pop()
                prev = prev.next

            prev.next = cur
            return tail  # Return the new end of this segment

        length = get_length(head)
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        while length >= k:
            head = reverse_k_nodes(prev, head, k)
            prev = head
            if head:
                head = head.next
            length -= k

        return dummy.next

