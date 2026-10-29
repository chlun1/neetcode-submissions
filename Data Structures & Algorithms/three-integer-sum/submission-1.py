class Solution:
    def twoSum(self, nums, start, target):
        l, r = start, len(nums) - 1
        res = set()
        while l < r:
            if nums[l] + nums[r] < target:
                l += 1
            elif nums[l] + nums[r] > target:
                r -= 1
            else:
                res.add((nums[l], nums[r]))
                l += 1
                r -= 1

        return list(res)

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums = sorted(nums)
        for i, num in enumerate(nums):
            pairs = self.twoSum(nums, i + 1, -num)
            for pair in pairs:
                res.add((num, pair[0], pair[1]))

        return list(res)
