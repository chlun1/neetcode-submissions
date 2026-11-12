# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a = headA
        b = headB

        len_a = 0
        while a:
            len_a += 1
            a = a.next

        len_b = 0
        while b:
            len_b += 1
            b = b.next

        a = headA
        b = headB

        for _ in range(len_a + len_b):
            if id(a) == id(b):
                return a

            a = a.next
            b = b.next

            if not a:
                a = headB
            if not b:
                b = headA

        return None
