# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            curr = curr.next
            length += 1

        n_groups = length // k
        dummy = ListNode(0, head)
        old_head = dummy
        curr = old_head.next

        for _ in range(n_groups):
            prev = None
            for _ in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            
            tmp = old_head.next
            old_head.next = prev
            old_head = tmp
            old_head.next = curr

        return dummy.next
