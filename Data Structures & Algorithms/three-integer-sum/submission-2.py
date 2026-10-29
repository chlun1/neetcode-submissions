class Solution:
    def twoSum(self, nums, start, target):
        l, r = start, len(nums) - 1
        res = []
        while l < r:
            if nums[l] + nums[r] < target:
                l += 1
            elif nums[l] + nums[r] > target:
                r -= 1
            else:
                res.append((nums[l], nums[r]))
                l += 1
                r -= 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1

        return res

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        for i, num in enumerate(nums):
            if num > 0:
                break
            if i > 0 and num == nums[i - 1]:
                continue
            pairs = self.twoSum(nums, i + 1, -num)
            for pair in pairs:
                res.append((num, pair[0], pair[1]))

        return res
