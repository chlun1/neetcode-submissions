class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2
            if mid + 1 < len(nums) and nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            elif mid > 0 and nums[mid] < nums[mid - 1]:
                return nums[mid]
            else:
                if nums[mid] > nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1

        return nums[0]
