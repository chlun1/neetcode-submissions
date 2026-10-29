class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = 0
        max_sum = nums[0]

        for num in nums:
            curr = max(curr + num, num)
            max_sum = max(max_sum, curr)

        return max_sum
        