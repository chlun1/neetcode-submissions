class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0, 0
        prev = None
        while r < len(nums):
            if nums[r] != prev:
                if l != r:
                    nums[l] = nums[r]
                prev = nums[l]
                l += 1
                r += 1
            else:
                r += 1

        return l
        