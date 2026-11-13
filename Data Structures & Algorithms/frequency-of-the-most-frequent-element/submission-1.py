class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()

        res = 1
        ops = 0
        l = 0

        for r in range(len(nums) - 1):
            needed = (nums[r + 1] - nums[r]) * (r - l + 1)
            ops += needed

            while ops > k:
                ops -= nums[r + 1] - nums[l]
                l += 1

            res = max(res, r - l + 2)

        return res
        