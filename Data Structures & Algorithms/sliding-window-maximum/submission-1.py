import heapq


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        r = k - 1
        res = []
        window = [(-nums[i], i) for i in range(l, r)]
        heapq.heapify(window)

        while r < len(nums):
            heapq.heappush(window, (-nums[r], r))

            while window[0][1] < l:
                heapq.heappop(window)

            res.append(-window[0][0])

            l += 1
            r += 1

        return res
        