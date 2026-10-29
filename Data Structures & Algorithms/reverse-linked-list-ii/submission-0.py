# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        old_head = dummy
        prev = None
        curr = head
        idx = 1
        
        while idx <= right:
            if idx >= left:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            else:
                curr = curr.next
                old_head = old_head.next
            idx += 1

        tmp = old_head.next
        old_head.next = prev
        tmp.next = next_node
        
        return dummy.next
