class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        subtotal = 0

        for i, num in enumerate(nums):
            if subtotal == total - subtotal - num:
                return i
            subtotal += num

        return -1
        