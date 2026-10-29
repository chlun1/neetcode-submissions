class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        sign = 0
        for i in range(1, len(nums)):
            if sign:
                if (
                    (sign == 1 and nums[i - 1] > nums[i])
                    or (sign == - 1 and nums[i - 1] < nums[i]) 
                ):
                    return False
            else:
                if nums[i - 1] < nums[i]:
                    sign = 1
                elif nums[i - 1] > nums[i]:
                    sign = -1

        return True
        