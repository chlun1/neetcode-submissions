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
            r = i
            tmp = nums[i]
            while True:
                r = (r + k) % n
                tmp, nums[r] = nums[r], tmp
                swapped += 1
                
                if r == i:
                    break
            i += 1
        