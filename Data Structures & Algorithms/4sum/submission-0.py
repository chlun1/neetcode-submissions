class Solution:
    def threeSum(self, nums, start, target):
        res = []
        for i in range(start, len(nums)):
            num = nums[i]
            if i > start and nums[i] == nums[i - 1]:
                continue
            new_target = target - num
            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] < new_target:
                    l += 1
                elif nums[l] + nums[r] > new_target:
                    r -= 1
                else:
                    res.append((num, nums[l], nums[r]))
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        return res

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            triples = self.threeSum(nums, i + 1, target - num)
            for a, b, c in triples:
                res.append([num, a, b, c])

        return res
