class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if (
                mid == 0 or mid == len(nums) - 1
                or (nums[mid - 1] != nums[mid] and nums[mid] != nums[mid + 1])
            ):
                return nums[mid]

            # If position (1-indexed) is odd then nums[mid] should be the
            # first of its pair. If not then its been shifted by a unique
            # element inserted before it.
            if mid % 2 == 0:
                if nums[mid] != nums[mid + 1]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] != nums[mid - 1]:
                    r = mid - 1
                else:
                    l = mid + 1
