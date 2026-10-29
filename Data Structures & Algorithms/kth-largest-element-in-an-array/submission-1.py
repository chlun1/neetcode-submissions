import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return min_heap[0]

    def findKthLargest_quickselect(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        def quick_select(l, r):
            pivot = nums[r]
            p = l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1

            nums[p], nums[r] = nums[r], nums[p]
            if p == k:
                return nums[p]
            if p < k:
                return quick_select(p + 1, r)
            else:
                return quick_select(l, p - 1)
        
        return quick_select(0, len(nums) - 1)
