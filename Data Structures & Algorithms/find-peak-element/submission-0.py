class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums = [-float("inf")] + nums + [-float("inf")]
        n = len(nums)
        l = 1
        r = n - 2

        while l <= r:
            m = l + (r - l) // 2

            if (
                nums[m - 1] < nums[m]
                and nums[m] > nums[m + 1]
            ):
                return m - 1

            if nums[m - 1] < nums[m] < nums[m + 1]:
                l = m + 1
            else:
                r = m - 1

        return -1
        