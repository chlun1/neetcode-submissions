class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        a, b = 0, nums[0]
        for i in range(1, len(nums)):
            a, b = b, max(b, a + nums[i])

        return b
