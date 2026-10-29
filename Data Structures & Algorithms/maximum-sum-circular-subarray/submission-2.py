class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_sum = nums[0]
        min_sum = nums[0]
        curr_min = 0
        curr_max = 0
        total = 0

        for num in nums:
            if curr_max < 0:
                curr_max = 0
            if curr_min > 0:
                curr_min = 0

            total += num
            curr_min += num
            curr_max += num
            max_sum = max(max_sum, curr_max)
            min_sum = min(min_sum, curr_min)

        return max(max_sum, total - min_sum) if max_sum > 0 else max_sum
        