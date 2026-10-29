# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        size = 0
        curr = head
        prev = None
        while curr:
            size += 1
            prev = curr
            curr = curr.next

        last = prev

        k %= size
        if k == 0:
            return head

        curr = head
        prev = None
        for _ in range(size - k):
            prev = curr
            curr = curr.next

        last.next = head
        prev.next = None

        return curr
