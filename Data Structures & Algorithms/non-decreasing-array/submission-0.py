class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        fixed_once = False

        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                if fixed_once:
                    return False

                if i > 0 and nums[i - 1] > nums[i + 1]:
                    nums[i + 1] = nums[i]
                else:
                    nums[i] = nums[i + 1]

                fixed_once = True

        return True
