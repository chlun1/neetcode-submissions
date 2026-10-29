# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        min_heap = [(node.val, i) for i, node in enumerate(lists) if node]
        heapq.heapify(min_heap)

        while min_heap:
            min_val, min_idx = heapq.heappop(min_heap)
            curr.next = lists[min_idx]
            curr = curr.next
            lists[min_idx] = lists[min_idx].next

            if lists[min_idx] is not None:
                heapq.heappush(min_heap, (lists[min_idx].val, min_idx))

        return dummy.next
        