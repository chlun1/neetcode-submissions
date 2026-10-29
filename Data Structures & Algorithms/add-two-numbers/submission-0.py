# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        curr = dummy

        while l1 and l2:
            val = l1.val + l2.val + carry
            curr.next = ListNode(val % 10)
            carry = val // 10
            curr = curr.next
            l1 = l1.next
            l2 = l2.next

        l = l1 or l2

        while l:
            val = l.val + carry
            curr.next = ListNode(val % 10)
            carry = val // 10
            curr = curr.next
            l = l.next

        if carry > 0:
            curr.next = ListNode(carry)

        return dummy.next
        