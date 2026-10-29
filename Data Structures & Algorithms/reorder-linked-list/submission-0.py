# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next:
            return

        # Get middle node
        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # Cut the original list in half
        prev.next = None
        
        # Reverse the second half
        prev = None
        curr = slow

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # Merge head and prev
        dummy = ListNode(-1)
        curr = dummy
        list1 = head
        list2 = prev

        while list1 and list2:
            curr.next = list1
            list1 = list1.next
            curr = curr.next

            curr.next = list2
            list2 = list2.next
            curr = curr.next

        curr.next = list1 or list2

        head = dummy.next
