class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = 0

        while r < n:
            num = nums[r]
            count = 0

            while r < n and nums[r] == num:
                count += 1
                r += 1

            for _ in range(min(2, count)):
                nums[l] = num
                l += 1
                
                if l == n:
                    break

        return l
