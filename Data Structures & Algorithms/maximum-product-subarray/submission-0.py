class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_min = 1
        curr_max = 1
        res = nums[0]

        for num in nums:
            new_curr_min = min(curr_min * num, curr_max * num, num)
            curr_max = max(curr_min * num, curr_max * num, num)
            curr_min = new_curr_min
            res = max(res, curr_max)

        return res
        