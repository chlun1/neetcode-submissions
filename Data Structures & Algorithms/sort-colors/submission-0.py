class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        curr = 0
        red = 0
        blue = len(nums) - 1

        while curr <= blue:
            if nums[curr] == 0:
                nums[curr], nums[red] = nums[red], nums[curr]
                red += 1
                curr += 1
            elif nums[curr] == 2:
                nums[curr], nums[blue] = nums[blue], nums[curr]
                blue -= 1
            else:
                curr += 1
