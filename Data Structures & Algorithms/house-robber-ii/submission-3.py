class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def helper(nums):
            a, b = 0, nums[0]
            for i in range(1, len(nums)):
                a, b = b, max(a + nums[i], b)

            return b

        return max(helper(nums[:-1]), helper(nums[1:]))
        