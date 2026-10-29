class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0, 0
        k = 0
        prev = None
        while r < len(nums):
            if nums[r] != prev:
                if l != r:
                    nums[l], nums[r] = nums[r], nums[l]
                prev = nums[l]
                k += 1
                l += 1
                r += 1
            else:
                r += 1

        return k
        