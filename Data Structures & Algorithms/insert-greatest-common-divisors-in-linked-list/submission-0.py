import math

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr.next:
            next_node = curr.next
            gcd = math.gcd(curr.val, next_node.val)
            curr.next = ListNode(gcd, next_node)
            curr = curr.next.next
        
        return head
            