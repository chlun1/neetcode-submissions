class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        swapped = 0
        i = 0
        while swapped < n:
            l, r = i, (i + k) % n
            tmp, nums[r] = nums[r], nums[l]
            swapped += 1
            while r != i:
                r = (r + k) % n
                tmp, nums[r] = nums[r], tmp
                swapped += 1

            i += 1
        